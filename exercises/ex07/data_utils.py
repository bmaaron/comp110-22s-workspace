"""Dictionary related utility functions."""

__author__ = "730530687"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row_oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(data: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Shows the first number of rows to ensure we are wrangling the data correctly."""
    result: dict[str, list[str]] = {}
    
    for items in data:
        values_in_column: list[str] = []
        i: int = 0
        if num_rows > len(data[items]):
            num_rows = len(data[items])
        while i < num_rows:
            values_in_column.append(data[items][i])
            i += 1
        result[items] = values_in_column
    return result
    

def select(data: dict[str, list[str]], specific_col: list[str]) -> dict[str, list[str]]:
    """Produces a new dict with a specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for value in data:
        if value in specific_col:
            result[value] = data[value]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce 1 new column table from 2 separate column tables."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            i: int = 0
            while i < len(table_2[column]):
                result[column].append(table_2[column][i])
                i += 1
            else:
                result[column] = table_2[column]
    return result


def count(counts: list[str]) -> dict[str, int]:
    """Counts the times a specified value has appeared in a list."""
    tot_count: dict[str, int] = {}
    for item in counts:
        if item in tot_count:
            tot_count[item] += 1
        else:
            tot_count[item] = 1
    return tot_count