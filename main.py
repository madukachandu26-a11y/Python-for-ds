""" This module for blablabla"""


import print_out

X_INIT: int = 1


def prog_integers(old_inventory: int, new_inventory: str) -> int:
    """summary_

    Args:
        num1 (int): _description_
        num2 (int): _description_

    Returns:
        int: _description_
    """
    y = old_inventory + new_inventory + X_INIT
    print_out.double_it(2) 
    return y


print(prog_integers(1, 2))