"""Test functions for dictionary.py."""

__author__ = "730530687"

from dictionary import invert


def test_normal_invert_use() -> None:
    """Tests the normal use."""
    a_dict = {"UNC": "Best", "Dukie": "worst", "NCSU": "mid"}
    assert invert(a_dict) == {"Best": "UNC", "worst": "Dukie", "mid": "NCSU"}


def test_non_unique_values() -> None:
    """Tests and returns a KeyError when there are the same values."""
    a_dict = {"A": "Yo", "B": "Yo"}
    assert invert(a_dict) == {} 
    
