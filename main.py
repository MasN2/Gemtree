import os
import discord
import pickle
from functions import *
import gem
import build

dir = r'C:\Path\to\Gemtree'

os.chdir(dir)

token_file = open('token.txt', 'r')

for token in token_file:
    TOKEN = token

client = discord.Client()

# a gem is represented as RPN, where a 1 is a basic gem and a 0 is combining the last two gems. When combining two different gems, the bigger number goes first.
try:
    with open("gems.pickle", 'rb') as f:
        client.tree = pickle.load(f)
        print("Database loaded.")
        print("------")
except FileNotFoundError:
    print("No database found. Making empty database.")
    print("------")
    client.tree = {0b1: gem.BasicGem}

def save_db(tree):
    with open("gems.pickle", 'wb') as f:
        pickle.dump(tree, f, protocol=2)
    print("Tree saved.")

def build_gem(gem_str):
    gem_int = int(gem_str, 2)
    if gem_int not in client.tree:
        a, b = build.gem_split(gem_str)
        client.tree[gem_int] = gem.combine(build_gem(a), build_gem(b))
    return client.tree[gem_int]

def populate():
    tree = set(client.tree)
    for x in tree:
        for y in tree:
            if x >= y:
                build_gem(bin(x)[2:] + bin(y)[2:] + "0")

@client.event
async def on_message(message):
    if not message.content.startswith("g!"):
        return
    message.content = message.content[2:]

    if message.content == "parameters":
        await client.send_message(message.channel, str(gem.parameters))
        return
    if message.content.startswith("list"):
        arg = argument_of(message.content)
        if not arg:
            msg_parts = ["```", f"{'Growth':7} Name"]
            for key, value in sorted(client.tree.items(), key=lambda x: gem.growth(x[1]), reverse=True):
                msg_parts += [f"{gem.growth(value):7.5f} {bin(key)}"]
            msg_parts += ["```"]
            await client.send_message(message.channel, "\n".join(msg_parts))
            # await client.send_message(message.channel, str([bin(x) for x in sorted(client.tree)]))
            return
        else:
            try:
                g = client.tree[int(arg, 2)]
            except (ValueError, KeyError):
                await client.send_message(message.channel, f"We do not have this gem in our database.")
                return
            else:
                await client.send_message(message.channel, f"{arg}:\n{g}")
                return

    # if message.content == "populate":
    #     populate()
    #     msg_parts = ["```", f"{'Growth':7} Name"]
    #     for key, value in sorted(client.tree.items(), key=lambda x: gem.growth(x[1]), reverse=True):
    #         msg_parts += [f"{gem.growth(value):7.5f} {bin(key)}"]
    #         if len(msg_parts) > 40:
    #             break
    #     msg_parts += ["```"]
    #     await client.send_message(message.channel, "\n".join(msg_parts))
    #     return

    if message.content == "save":
        save_db(client.tree)
        await client.send_message(message.channel, "Successfully saved.")
        return

    if message.content.startswith("combine"):
        try:
            args = argument_of(message.content)
            arg1, arg2 = peel(args)
            gid1, gid2 = int(arg1, 2), int(arg2, 2)
            if gid1 < gid2:
                arg1, arg2 = arg2, arg1
                gid1, gid2 = gid2, gid1
            g1, g2 = client.tree[gid1], client.tree[gid2]
        except (ValueError, KeyError):
            await client.send_message(message.channel, f"We do not have these gems in our database.")
            return
        else:
            gid3 = int(arg1 + arg2 + "0", 2)
            client.tree[gid3] = gem.combine(g1, g2)
            await client.send_message(message.channel, f"{bin(gid3)}:\n{client.tree[gid3]}")
            return

    if message.content.startswith("build"):
        try:
            arg = argument_of(message.content)
            result_gem = build_gem(arg)
        except ValueError:
            await client.send_message(message.channel, "Invalid gem string.")
            return
        else:
            await client.send_message(message.channel, f"0b{arg}:\n{result_gem}")



@client.event
async def on_ready():
    print('Logged in as ' + client.user.name)
    print('ID: ' + str(client.user.id))
    print('------')
client.run(TOKEN)
