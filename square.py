"""
Complete the square sum function 
so that it squares each number passed into it 
and then sums the results together.

"""

numbers = [1,5,2]

def square_sum(numbers):
    squared_list = [number**2 for number in numbers]
    return sum(squared_list)
    
print(square_sum(numbers))