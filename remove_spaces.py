# Write a function that removes the spaces from the string, then return the resultant string.

def no_space(x):
    new_string = x.replace(' ', '')
    return new_string

remove_space = no_space('this is a string')
print(remove_space)