'''
2.Find the odd int

Instructions

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time

'''

#solution 1
#1.循环计算每一个元素的个数
#2.遇到为单数的则返回
def find_it(seq):
    for x in seq:
        if(seq.count(x)%2==1):
            return x
    return None



#solution 2
#1.循环计算每一个元素的个数,条件为每一元素的计数为单数
#2.返回列表第一个元素
def find_it(seq):
    return [x for x in seq if seq.count(x)%2!=0][0]


#solution 3
#1.对列表每一个元素使用异或运算,偶数个的数异或之后为0,最后只剩下奇数的值
#2.使用functiools库中的reduce对列表每个元素执行运算,运算方式为xor
import functools
import operator
def find_it(seq):
    return functools.reduce(operator.xor,seq)