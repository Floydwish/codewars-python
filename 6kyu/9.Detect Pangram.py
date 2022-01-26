'''
9.Detect Pangram

Instructions

A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
Ignore numbers and punctuation.

'''

#solution 1
#0.筛选出字母,使用string的isalpha
#1.统一转小写,使用lower
#2.去重,使用set
#3.排序,使用sort
#4.比较
import string

def is_pangram(s):
    lis = list("abcdefghijklmnopqrstuvwxyz")
    ss = ''.join(c for c in s if c.isalpha()).lower()
    l=list(set(ss))
    l.sort()

    return l==lis


#solution 2
#1.使用string的ascii_lowercase生成小写字母表串
#2.使用lower()将s转为小写
#3.将二者分别构造为set,若字母表串<=s,则为pangram
#注：
#1.set中会自动排序比较
#2.ascii中空格、标点等均小于字母,只要s中缺少一个字母,比较结果就为False
import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())


#solution 3
#1.使用string的ascii_lowercase生成小写字母表串
#2.使用lower()将s转为小写
#3.使用issubset()判断字母表是否为s的子set
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))


#solution 4
#1.循环查找法
#2.遍历字母表(转换角度)
import string

def is_pangram(s):
    ss=s.lower()
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in ss:
            return False
    return True



