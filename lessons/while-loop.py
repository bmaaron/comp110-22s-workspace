"""An example of a while loop statement."""

__author__ = "730530687"

counter: int = 0
maximum: int = int(input("Count up to, but not including what? "))

while counter < maximum:
    counter_squared: int = counter ** 100000
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter - 1000

print("Done!")
