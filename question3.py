# Design a function that takes a string or sequence of characters as input and
# returns the character that appears most frequently.
# //Eg 11189 => '1'
# //hello => l
from collections import Counter


def return_most_frequent(value):
    return Counter(value).most_common(1)[0][0]


# Example
print(return_most_frequent("11189"))
print(return_most_frequent("hello"))
