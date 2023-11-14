"""
Write a function named set_alarm which receives two parameters. 
The first parameter, employed, is true whenever you are employed 
and the second parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

employed | vacation 
true     | true     => false
true     | false    => true
false    | true     => false
false    | false    => false
"""

def set_alarm(employed, vacation):
    # Check if employed is True
    if employed == True:
        # Check if vacation is also True
        if vacation == True:
            # If both employed and on vacation, return False
            return False
        # If employed is True and not on vacation, return True
        elif vacation == False:
            return True
    # If not employed, regardless of vacation status, return False
    else:
        # Check if on vacation when not employed, return False
        if vacation == True:
            return False
        # If not employed and not on vacation, return False
        return False
    
# OR

def set_alarm_2(employed, vacation):
    # Return the result of the logical expression employed and not vacation
    # This expression evaluates to True only if employed is True and vacation is False
    # If employed and not on vacation, the function returns True; otherwise, it returns False
    return employed and not vacation

    
# Test cases
print(set_alarm(True, True))    # Output: False
print(set_alarm(True, False))   # Output: True
print(set_alarm(False, True))   # Output: False
print(set_alarm(False, False))  # Output: False

print(set_alarm_2(True, True))    # Output: False
print(set_alarm_2(True, False))   # Output: True
print(set_alarm_2(False, True))   # Output: False
print(set_alarm_2(False, False))  # Output: False