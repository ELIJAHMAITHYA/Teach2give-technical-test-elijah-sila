# Master Yoda, a renowned Jedi Master from the Star Wars universe, is known
# for his unique way of speaking. He often reverses the order of words in his
# sentences. For example, instead of saying "I am home" he might say "Home
# am I" Design a function that takes a sentence as input and returns a new
# sentence with the words reversed in the same order that Master Yoda would
# use.

def master_yoda_speak(statement):
    words = statement.split()
    reversed_words = words[::-1]

    reversed_statement = ' '.join(reversed_words)
    return reversed_statement


# Examples
print(master_yoda_speak("I am home"))
print(master_yoda_speak("Hello there"))
