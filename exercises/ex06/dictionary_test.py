"""Test functions for dictionary.py."""

__author__ = "730530687"

from dictionary import invert
from exercises.ex06.dictionary import favorite_color


def test_normal_invert_use() -> None:
    """Tests the normal use."""
    a_dict = {"UNC": "Best", "Dukie": "worst", "NCSU": "mid"}
    assert invert(a_dict) == {"Best": "UNC", "worst": "Dukie", "mid": "NCSU"}


def test_single_key_value_use() -> None:
    """Tests for when there is only one item in the dict."""
    a_dict = {"A": "Yo"}
    assert invert(a_dict) == {"Yo": "A"}
    

def test_empty_dict_edge() -> None:
    """Tests to ensure the return is an empty list when the input is an empty list."""
    a_dict = {}
    assert invert(a_dict) == {}


def test_favorite_colors_norm_use() -> None:
    """Tests to ensure the fxn is working properly."""
    a_dict = {"Matt": "Blue", "Mark": "Blue", "Luke": "Yellow", "John": "Green"}
    assert favorite_color(a_dict) == 'Blue'


def test_favorite_colors_two_winning_colors_edge() -> None:
    """Tests to ensure the correct color is printed."""
    a_dict = {"Matt": "Blue", "Mark": "Blue", "Luke": "Yellow", "John": "Yellow"}
    assert favorite_color(a_dict) == 'Blue'


def test_favorite_colors_large_list_use() -> None:
    """Tests to ensure with a large list it still functions correctly."""
    a_dict = {"a": "green", "b": "blue", "c": "yellow", "d": "green", "e": "green", "f": "red"}
    assert favorite_color(a_dict) == 'green'