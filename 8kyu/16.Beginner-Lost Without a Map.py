'''
16.Beginner-Lost Without a Map

Instructions

Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''

#solution 1
#1.循环修改list并返回
def maps(a):
    return [x*2 for x in a]



#solution 2
#1.使用map进行映射,lambda代替映射函数
#2.将结果转为list
def maps(a):
    return list(map(lambda x : 2*x, a))