"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

def accum(s):
    # Initialize an empty result string
    result = ""
    
    # Iterate through the characters in the input string
    for i, char in enumerate(s):
        # Append the current character in uppercase
        result += char.upper()
        
        # Append the current character repeated (i+1) times in lowercase
        result += char.lower() * i
        
        # Add a hyphen if it's not the last character
        if i < len(s) - 1:
            result += "-"
    
    return result

# Test cases
print(accum("abcd"))     # Output: "A-Bb-Ccc-Dddd"
print(accum("RqaEzty"))  # Output: "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(accum("cwAt"))     # Output: "C-Ww-Aaa-Tttt"
