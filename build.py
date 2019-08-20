from typing import Tuple

# "1101010" -> ("11010", "1")
def gem_split(a: str) -> Tuple[str, str]:
    if a[-1] != '0':
        raise ValueError
    position = len(a) - 1
    balance = 1
    for n in reversed(a[:-1]):
        position -= 1
        if n == '0':
            balance += 1
        elif n == '1':
            balance -= 1
        else:
            raise ValueError
        if balance == 0:
            break
    rv = a[:position], a[position:-1]
    if int(rv[0], 2) < int(rv[1], 2):
        raise ValueError
    return rv
