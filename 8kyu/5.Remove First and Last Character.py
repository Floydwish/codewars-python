
'''
5.Remove First and Last Character

Instructions

It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

'''

//solution 1
//1.使用切片获取子串
//2.用到len计算string的字符数
//3.去头去尾截取中间
def remove_char(s):
    return s[1 : len(s)-1]


//solution 2
//1.使用切片获取子串
//2.使用-1作为倒数第2个位置
//3.去头去尾截取中间
def remove_char(s):
    return s[1 : -1]

//solution 3
//1.使用list的pop接口
//2.去头去尾取中间
def remove_char(s):
    s1 = list(s)
    s1.pop(0)
    s1.pop()
    return ''.join(s1) 