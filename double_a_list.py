"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

"""

def maps(a):
    return [2*x for x in a]

print(maps([1,2,3]))

# The function takes the input array a, doubles each value in the array using the list comprehension, and returns the new array with the doubled values.