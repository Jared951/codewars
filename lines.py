"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings 
and returns each line prepended by the correct number.

The numbering starts at 1. 
The format is n: string. 
Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
"""

def number(lines):
    # Create an empty list to store the result
    result = []

    # Enumerate through each line, starting the numbering from 1
    for i, line in enumerate(lines, start=1):
        # Format each line with its corresponding number and append to the result list
        formatted_line = f"{i}: {line}"
        result.append(formatted_line)

    # Return the final result
    return result


print(number({"a", "b", "c"}))