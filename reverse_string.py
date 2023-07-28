"""
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'

"""

def solution(string):
    str = ""
    for i in string:
        str = i + str
    return str

print(solution("this is it"))