'''
17.Invert values

Instructions

Given a set of numbers, return the additive inverse of each. 
Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list.

'''

#solution 1
#1.使用循环
def invert(lst):
    l=list()
    for x in lst:
        l.append(-1*x)
    return l


#solutino 2
#1.使用循环
def invert(lst):
    return [-x for x in lst]


#solutino 3
#1.先使用map映射每一个lst元素
#2.将映射后的元素转为list
def invert(lst):
    return list(map(lambda x:-x,lst))
