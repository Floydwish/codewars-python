'''
18.Odd or Even?

Instructions

Task:
Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Examples:
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"

Have fun!

'''

#solution 1
#1.计算列表中元素的和,使用内置函数sum
#2.判断奇、偶,返回对应字串
def odd_or_even(arr):
    s = sum(arr)
    return "even" if s%2==0 else "odd"


#solution 2
#1.计算列表中元素的和,使用内置函数sum
#2.判断奇、偶,返回对应字串
def odd_or_even(arr):
    return "even" if sum(arr)%2==0 else "odd"


#solution 3
#0.最朴素的方法
#1.计算列表中元素的和
#2.判断奇、偶,返回对应字串
def odd_or_even(arr):
    s = 0
    for i in arr:
        s+=i
    if s%2 == 0:
        return "even"
    else:
        return "odd"

#solution 4
#1.计算列表中元素的和,使用sum
#2.判断奇、偶,返回对应字串,使用元祖+下标
def odd_or_even(arr):
    return ("even","odd")[sum(arr)%2]
