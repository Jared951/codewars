"""
In this kata you will create a function 
that takes a list of non-negative integers 
and strings 
and returns a new list 
with the strings filtered out.
"""

def filter_list(lst):
    # Use a list comprehension to iterate through each element in the input list (lst)
    # Include only elements that are instances of integers (filter out strings)
    return [x for x in lst if isinstance(x, int)]

# Example usage:
input_list = [1, 2, 'a', 'b', 3]
result = filter_list(input_list)

# Print the result
print(result)