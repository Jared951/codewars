"""

You are given an array(list) strarr of strings and an integer k. 
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

"""

def longest_consec(strarr, k):
    # Get the length of the input array
    n = len(strarr)
    
    # Check for edge cases: empty array, k greater than array length, or k less than or equal to 0
    if n == 0 or k > n or k <= 0:
        return ""
    
    # Initialize variables to store the maximum length and the corresponding result
    max_length = 0
    result = ""
    
    # Iterate through the array
    for i in range(n - k + 1):
        # Concatenate k consecutive strings
        current_str = ''.join(strarr[i:i+k])
        
        # Calculate the length of the current concatenated string
        current_length = len(current_str)
        
        # Update the result if the current length is greater than the maximum length
        if current_length > max_length:
            max_length = current_length
            result = current_str
    
    # Return the final result
    return result

# Examples
strarr1 = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k1 = 2
print(longest_consec(strarr1, k1))  # Output: "folingtrashy"

strarr2 = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
k2 = 2
print(longest_consec(strarr2, k2))  # Output: "abigailtheta"

