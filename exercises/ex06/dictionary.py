"""Skeltons for dictionary test functions."""

__author__ = "730530687"

from collections import Counter


def invert(a_dict: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and inverts the keys and values."""
    b_dict = {value: key for (key, value) in a_dict.items()}
    if len(a_dict) != len(b_dict):
        raise KeyError
    
    return b_dict


def favorite_color(a_dict: dict[str, str]) -> str:
    """Takes a dict of persons fav colors and returns the most popular color."""
    count_of_colors = Counter(a_dict.values())
    # for key, value in count_of_colors.items():
    return ([key for key in count_of_colors.keys()][0])


def count(a_list: list[str]) -> dict[str, int]:
    """Counts the number of times an item has appeared in a list."""
    empty_dict: dict[str, int] = {}
    for i in a_list:
        if i in empty_dict:
            empty_dict[i] += 1
        else:
            empty_dict[i] = 1
    return empty_dict