'''
When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.
'''

def switch_it_up(number):
    # Define a dictionary to map numbers to words
    num_to_word = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    # Check if the number is in the dictionary, and return the corresponding word
    if number in num_to_word:
        return num_to_word[number]
    else:
        return "Number out of range"

# Test cases
print(switch_it_up(1))  # Output: "One"
print(switch_it_up(9))  # Output: "Nine"
print(switch_it_up(12)) # Output: "Number out of range"