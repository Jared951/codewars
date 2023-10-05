"""
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
Note: The order of the permutations doesn't matter.

"""

def permutations(s):
    def backtrack(start):
        if start == len(s):
            permutations_set.add("".join(s))
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]  # Swap characters at positions 'start' and 'i'
            backtrack(start + 1)  # Recursively generate permutations for the rest of the string
            s[start], s[i] = s[i], s[start]  # Undo the swap to backtrack and try the next possibility

    s = list(s)  # Convert the input string to a list of characters for easier manipulation
    permutations_set = set()
    backtrack(0)
    return list(permutations_set)

print(permutations('a'))      
print(permutations('ab'))     
print(permutations('abc'))    
print(permutations('aabb')) 

# or

import itertools

def permutations_two(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

print(permutations_two('a'))      
print(permutations_two('ab'))     
print(permutations_two('abc'))    
print(permutations_two('aabb')) 