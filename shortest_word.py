"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(s):
    # Split the input string into words
    words = s.split()
    
    # Initialize a variable to keep track of the shortest word length
    shortest_length = float('inf')  # Initialize to positive infinity
    
    # Iterate through the words and update the shortest_length if needed
    for word in words:
        word_length = len(word)
        if word_length < shortest_length:
            shortest_length = word_length
    
    return shortest_length

# Test cases
print(find_short("This is a test"))  # Output: 1 (Shortest word is "a")
print(find_short("These are some words"))  # Output: 3 (Shortest word is "are")
print(find_short("bitcoin take over the world maybe who knows perhaps"))  # Output: 3 (Shortest word is "the")


# OR

def find_short_two(s):
    return min(len(x) for x in s.split())