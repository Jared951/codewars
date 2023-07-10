"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

"""

def reverse_words(text):
    words = text.split(' ') # split the text into individual words
    reversed_words = [word[::-1] for word in words] # reverse each word
    reversed_text = ' '.join(reversed_words) # join the reversed words with spaces
    return reversed_text

print(reverse_words('this is a test'))