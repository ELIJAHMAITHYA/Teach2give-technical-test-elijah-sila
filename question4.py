# Design a function that determines whether a given string is a pangram. A
# pangram is a sentence or phrase containing every letter of the alphabet at
# least once. Punctuation and case are typically ignored. For example, the
# string "The quick brown fox jumps over the lazy dog" is a pangram, while
# "Hello, world!" is not.
import string

def check_if_pangram(value):
    alphabet_set = set(string.ascii_lowercase)
    input_set = set(c.lower() for c in value if c.isalpha())

    return alphabet_set <= input_set


# Examples
print(check_if_pangram("The quick brown fox jumps over the lazy dog"))
print(check_if_pangram("Hello, world!"))
