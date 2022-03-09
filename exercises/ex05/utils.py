"""Function skeltons and implementations."""

__author__ = "730530687"


def only_evens(nums: list[int]) -> list[int]:
    """Returns only the even #'s in a list of ints."""
    i: int = 0
    length: int = len(nums)
    even_nums: list[int] = list()
    while i < length:
        remainder: float = nums[i] % 2
        if remainder == 0:
            even_nums.append(nums[i])
        i += 1
    return even_nums


def sub(a_list: list[int], x: int, y: int) -> list[int]:
    """Generates a list between start index (x) and end index (y)."""
    if y > len(a_list):
        return a_list[x:len(a_list)]
    if x < 0:
        return a_list[0:y]
    if len(a_list) == 0:
        return a_list
    else:
        return a_list[x:y]


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Generates a list with the elements of only_evens and sub defs."""
    nums: list[int] = []
    a_list: list[int] = []
    concat_list: list[int] = list()
    # part_1_list: list[int] = list()
    # part_2_list: list[int] = list()
    
    # part_1_list = only_evens(nums)
    # part_2_list = sub(a_list, 1, 3)
    # concat_list = part_1_list + part_2_list
    # return concat_list

    concat_list = only_evens(nums) + sub(a_list, 1, 3)
    return concat_list