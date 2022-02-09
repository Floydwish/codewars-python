'''
11.Break camelCase

Instructions

Complete the solution so that the function will break up camel casing, 
using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

'''

#solution 1
#1.循环,当遇到大写字母时,添加空格
#3.每次循环都把字母加到结果string
def solution(s):
    res=''
    for char in s:
        if char.isupper():
            res+=' '
        res+=char
    return res

#solution 2
#1.使用enumerate得到index-value对
#2.循环给定string的index-value对,当遇到大写字母时,添加空格
#3.每次循环都把字母加到结果string
def solution(s):
    res=''
    for i,char in enumerate(s):
        if i and char.isupper():
            res+=' '
        res+=char
    return res


#solution 3
#1.循环,当遇到大写字母时,添加空格
#3.使用join把字母加到结果string
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
