"""Skeltons for dictionary test functions."""

__author__ = "730530687"


def invert(a_dict: dict[str, str]) -> dict[str, str] or str:
    """Takes a dictionary and inverts the keys and values."""
    i: int = 0
    a_dict = {value: key for (key, value) in a_dict.items()}
   
    while i < len(a_dict):
        if a_dict.values() == a_dict.values:
            print("raise KeyError (Values must be unique strings!")
    return a_dict
