"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730530687"


class Simpy:
    """A utility class for working with a column of numerical values."""
    values: list[float] = []

    def __init__(self, values: list): 
        """Initializes the Simpy Class."""
        self.values = values 
    
    def __str__(self) -> str:
        """Produce a str representation of the Simpy Values."""
        return f"Simpy({self.values})"

    def fill(self, value: float, nums_in: int) -> None:
        """Fills a Simpy's values with a specific # of repeating values."""
        self.values.clear() 
        for i in range(nums_in):
            self.values.append(value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Starts a list at the start float, increments by the step attribute and stops at stop."""
        assert step != 0.0
        while start != stop:
            self.values.append(start)
            start += step
            
    def sum(self) -> float:
        """Sums the ints in the values list."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds the self.values at [i] to rhs [i] if a list or adds the rhs int to self.values at each [i]."""
        result: list[float] = []
        for i in range(len(self.values)):
            if isinstance(rhs, float):
                result.append(self.values[i] + rhs)
            else: 
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponates the self.values at [i] with respect to rhs [i] if a list."""
        result: list[float] = []
        for i in range(len(self.values)):
            if isinstance(rhs, float):
                result.append(self.values[i] ** rhs)
            else: 
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Makes a bool mask based on the equality of other value attributes and returns a list of bools."""
        result: list[bool] = []
        for i in range(len(self.values)):
            if isinstance(rhs, float):
                if rhs == self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
            else: 
                if rhs.values[i] == self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Makes a bool mask based on the greater than relationship of other value attributes and returns a list of bools."""
        result: list[bool] = []
        for i in range(len(self.values)):
            if isinstance(rhs, float):
                if rhs < self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
            else: 
                if rhs.values[i] < self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Takes a list of bools and returns a new simpy object with the masked values."""
        result: list[float] = []
        i: int = 0
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            while i < len(rhs):
                if rhs[i]:
                    result.append(self.values[i])
                i += 1
        return Simpy(result)
        