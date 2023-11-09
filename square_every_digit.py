"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!
"""

def square_digits(num):
    # Convert the input number to a string to iterate over its digits
    num_str = str(num)
    result = ''

    for digit in num_str:
        squared_digit = int(digit) ** 2
        result += str(squared_digit)

    # Convert the result back to an integer before returning it
    return int(result)

print(square_digits(9119))  # Output: 811181
