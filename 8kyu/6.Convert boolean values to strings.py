'''
6.Convert boolean values to strings 'Yes' or 'No'.

Instructions

Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

'''

//solution 1
//1.条件判断
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"


//solution 2
//1.三元条件判断
def bool_to_word(boolean):
    return "Yes" if boolean else "No"