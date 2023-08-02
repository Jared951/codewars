"""
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"

"""

def repeat_str(repeat, string):
    return string * repeat

# The function takes the input repeat (an integer) and string (a string) and returns the repeated string. 
# The multiplication operator * is used to repeat the string repeat times.


print(repeat_str(6, "I"))  # Output: "IIIIII"
print(repeat_str(5, "Hello"))  # Output: "HelloHelloHelloHelloHello"