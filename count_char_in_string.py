"""
The main idea is to count all the occurring characters in a string. 
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

# Define a function named 'count' that takes a single argument 's' (a string).
def count(s):
    # Initialize an empty dictionary named 'char_count' to store character counts.
    char_count = {}
    
    # Iterate over each character in the input string 's'.
    for char in s:
        # Check if the character 'char' is already a key in 'char_count'.
        if char in char_count:
            # If the character is already in 'char_count', increment its count by 1.
            char_count[char] += 1
        else:
            # If the character is not in 'char_count', add it as a key with a count of 1.
            char_count[char] = 1
    
    # Return the 'char_count' dictionary containing character counts.
    return char_count

# Call the 'count' function with the input string 'aabbcc'.
result = count('aabbcc')

# Print the result, which will be a dictionary with character counts.
print(result)

# or

from collections import Counter

def count_two(string):
    return Counter(string)