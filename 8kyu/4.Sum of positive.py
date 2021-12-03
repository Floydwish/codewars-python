'''
4.Sum of positive

Instructions
Output
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
'''

//solution 1
def positive_sum(arr):
    sum=0
    for n in arr:
        if n>0:
            sum+=n
    return sum


//solution 2
def positive_sum(arr):
    return sum(x for x in arr if x>0)


'''
solution 2 note:
it's a generator expression. Instead of creating a list of all elements it creates an iterable object that 
returns a single element at a time, which sum() can still operate on. You could also add square brackets and
 it should still work (because both lists and generator objects are iterable) but will use more memory.
'''