"""
You ask a small girl,"How old are you?" She always says, "x years old", 
where x is a random number between 0 and 9.

Write a program that returns the girl's age (0-9) as an integer.

Assume the test input string is always a valid string. 
For example, the test input may be "1 year old" or "5 years old". 
The first character in the string is always a number.
"""

def get_age(age):
    # Split the input string into words
    words = age.split()
    # Extract the first word, which should be the age
    age_word = words[0]
    # Convert the age word to an integer
    age = int(age_word)

    return age

test_input = "3 years old"  # Replace with any valid input string
girl_age = get_age(test_input)
print(f"The girl is {girl_age} years old.")