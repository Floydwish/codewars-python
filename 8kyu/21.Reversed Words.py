'''
21.Reversed Words

Instructions

Complete the solution so that it reverses all of the words within the string passed in.

Example:

"The greatest victory is that which requires no battle" --> "battle no requires which 
that is victory greatest The"

'''

#solution 1
#1.将string分割为list
#2.使用str的reverse()翻转list
#3.使用空格连接list中各单词
def reverse_words(s):
    l = s.split(" ")
    l.reverse()
    return ' '.join([x for x in l])


#solution 2
#1.将string分割为list
#2.使用切片逆序取出list中的单词 (s[start:stop:step])
#3.使用空格连接list中各单词
def reverse_words(s):
    return ' '.join(s.split(" ")[::-1])


#solution 3
#1.将string分割为list
#2.使用reversed()翻转list
#3.使用空格连接list中各单词
def reverse_words(s):
    return ' '.join(reversed(s.split(' ')))





