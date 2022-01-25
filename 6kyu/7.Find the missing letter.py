'''
7.Find the missing letter

Instructions

#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and 
that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. 
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!


test.describe("kata tests")
test.it("example tests")
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')

'''

#solution 1
#1.ord返回字符的ASCII码,chr相反
#2.循环判断相邻字符的差值,差值大于1则判断为找到缺失字符
#3.在前值基础上加1后转为字符返回
def find_missing_letter(chars):
    for i in range(len(chars)-1):
        if ord(chars[i])-ord(chars[i+1]) != -1:
            return chr(ord(chars[i])+1)
    return ''


#solution 2
#1.使用列表查找方式
#2.根据输入列表找出字母列表的起始位置
#3.循环比较,不相等的字符即为缺失字符
def find_missing_letter(chars):
    l = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = l.index(chars[0])
    for i in range(0,len(chars)):
        if chars[i] != l[i+start]:
            return l[i+start]