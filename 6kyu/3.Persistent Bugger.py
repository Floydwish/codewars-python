'''
3.Persistent Bugger.

Instructions

Write a function, persistence, that takes in a positive parameter num and 
returns its multiplicative persistence, which is the number of times you must 
multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)

'''
#solution 1
#0.双循环
#1.将数值转为string,转为list
#2.循环遍历并累乘
def persistence(n):
    num = n
    cnt = 0;
    while(True):
        count=1
        if num//10==0:
            return cnt
        for x in list(str(num)):
            count*=int(x)
        else:
            num = count
            cnt+=1


#solution 2 - 优化solution 1
#0.双循环
#1.将数值转为string
#2.循环遍历并累乘
#3.内层循环累乘结果作为下一次外层循环的参数
def persistence(n):
    cnt = 0
    s = str(n)
    while len(s)>1:
        count = 1
        for x in s:
            count*=int(x)
        s=str(count)
        cnt+=1
    return cnt


#operation 3
#1.循环计算每一次各数位相乘的结果(2位数及以上)
#2.使用functool的reduce接口对每一个list成员进行连乘, operator.mul作为转换方法
#3.数字统一转为string,再对每一位转为int

import functools
import operator

def persistence(n):
    cnt = 0
    while n>=10:
        n = functools.reduce(operator.mul,[int(x) for x in str(n)])
        cnt+=1
    return cnt
