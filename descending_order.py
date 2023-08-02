"""
Your task is to make a function that can take any non-negative integer as an argument 
and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321


"""

def descending_order(num):
    # Convert the number to a string and sort its characters in descending order
    sorted_digits = sorted(str(num), reverse=True)
    
    # Join the sorted characters and convert back to an integer
    sorted_num = int(''.join(sorted_digits))
    
    return sorted_num

# Test cases
print(descending_order(42145))    # Output: 54421
print(descending_order(145263))   # Output: 654321
print(descending_order(123456789))# Output: 987654321