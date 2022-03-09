"""Test functions for utils.py."""

__author__ = "730530687"

from utils import only_evens, sub, concat


def test_only_evens_normal_use() -> None:
    """Tests the normal use."""
    nums: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert only_evens(nums) == [2, 4, 6]


def test_only_evens_single_item_edge() -> None:
    """Tests only a single item."""
    nums: list[int] = [1]
    assert only_evens(nums) == []


def test_only_evens_zero_items_edge() -> None:
    """Tests no items in list."""
    nums: list[int] = []
    assert only_evens(nums) == []


def test_only_evens_only_odds_use() -> None:
    """Tests only odds."""
    nums: list[int] = [1, 3, 5, 7]
    assert only_evens(nums) == []


def test_sub_norm_use() -> None:
    """Tests the norm use."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 6) == [20, 30, 40]


def test_sub_zero_items_edge() -> None:
    """Tests no items."""
    a_list: list[int] = []
    assert sub(a_list, -1, 3) == []


def test_sub_large_list_use() -> None:
    """Tests a large list."""
    a_list: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert sub(a_list, -4, 7) == [10, 20, 30, 40, 50, 60, 70]


def test_sub_large_y_input_edge() -> None:
    """Tests a large y input so the fxn will return last int."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 9) == [20, 30, 40]


def test_concat_norm_use() -> None:
    """Tests the concat norm use."""
    nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a_list: list[int] = [10, 20, 30, 40]
    assert concat(nums, a_list) == [2, 4, 6, 8, 10, 20, 30]