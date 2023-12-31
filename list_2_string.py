"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. 
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.


"""

def likes(names):
    # Check if the input list is empty (no one likes this)
    if len(names) == 0:
        return "no one likes this"
    # Check if there is only one name (e.g., "Peter likes this")
    elif len(names) == 1:
        return f"{names[0]} likes this"
    # Check if there are two names (e.g., "Jacob and Alex like this")
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    # Check if there are three names (e.g., "Jacob, Alex and Mark like this")
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    # For four or more names, display the first two names and count of others (e.g., "Alex, Jacob and 2 others like this")
    else:
        others_count = len(names) - 2
        return f"{names[0]}, {names[1]} and {others_count} others like this"

# Test cases
print(likes([]))  # "no one likes this"
print(likes(["Peter"]))  # "Peter likes this"
print(likes(["Jacob", "Alex"]))  # "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"]))  # "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"]))  # "Alex, Jacob and 2 others like this"

