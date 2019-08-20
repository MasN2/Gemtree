# Gemtree
Discord bot for gem combining for GC2

To run:
    python c:\Path\to\Gemtree\main.py %*

Make sure:
* you have discord.py
* the dir in main.py includes your actual path to gemtree
* you have a TOKEN.txt file with your discord bot's token

I didn't include help commands in the bot, so here's the commands:

First, note that every gem is represented as a string of 1s and 0s, where a 1 is a basic gem and a 0 is a merger of the last two gems.

> parameters

Outputs a list of the combination rules.

> list

Shows a list of the gems known, ordered by their efficiency.

> list <#>

Shows the details of gem <#>

> save

Stores the gem database to file for loading later.

> combine # #

Combines the two given gems, adds it to the database, and shows the results.

> build #

Creates the target gem, adding to the database it and all intermediate components. Shows the result. If the gem is already in the database, shows it.

Included in the code is a commented-out populate command. This command populates the database by combining all possible pairs of gems. Enabled at your own risk; your discord client may time out while the program attempts to handle the command. In addition, the command used multiple times will create LARGE databases. 
