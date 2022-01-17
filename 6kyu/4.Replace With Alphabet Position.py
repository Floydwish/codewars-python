'''
4.Replace With Alphabet Position

Instructions

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )\

'''

#solution 1
#1.将入参转为小写, 判断为字母的字符才处理
#2.循环遍历每个字符，使用ord将字符转为ASCII码,并作相应转换,每一个结果转为字符
#3.使用join连接结果字符
def alphabet_position(text):
    return ' '.join([str(ord(x)-ord('a')+1) for x in text.lower() if x.isalpha()])


#solution 2
#1.将入参转为小写, 判断为字母的字符才处理
#2.循环遍历每个字符，使用ord将字符转为ASCII码,并作相应转换,每一个结果转为字符
#3.使用join连接结果字符
def alphabet_position(text):
    return ' '.join([str(ord(x)-96) for x in text.lower() if x.isalpha()])

