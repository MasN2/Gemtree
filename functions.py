from typing import Tuple

def peel(x: str) -> Tuple[str, str]:
    parts = x.split(maxsplit=1)
    if len(parts) == 1:
        return parts[0], ""
    else:
        return parts[0], parts[1]


def argument_of(x: str) -> str:
    return peel(x)[1]