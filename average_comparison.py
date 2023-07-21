"""
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!

Note:
Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

"""

def better_than_average(class_points, your_points):
    # Calculate the sum of your classmate's test scores
    class_sum = sum(class_points)

    # Add your own test score to the sum
    total_sum = class_sum + your_points

    # Calculate the average
    num_students = len(class_points) + 1  # Add 1 to include yourself
    average = total_sum / num_students

    # Compare your score with the average
    return your_points > average

# Example usage:
your_score = 85
class_scores = [78, 90, 82, 88, 76]
result = better_than_average(class_scores, your_score)
print(result)  # This will output True or False based on whether you're better than the average.