'''
11.Century From Year

Instructions

Introduction
The first century spans from the year 1 up to and including the year 100, 
the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20

'''

#solution 1
#1.使用地板除
#2.当year%100余数为0时，结果为地板除，否则为地板除+1
def century(year):
    return year//100 if year%100==0 else year//100+1


#solution 2
#1.使用地板除
#2.根据2000为20世纪，而2001为21世纪的规律，作出转换：
#3.世纪 = (year+99)//100
def century(year):
    return (year+99)//100


#solution 3
#1.使用math模块的ceil()函数
#2.ceil():函数返回数字的上入整数
import math
def century(year):
    return math.ceil(year)