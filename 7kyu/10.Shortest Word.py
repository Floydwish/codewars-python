'''
10.Shortest Word

Instructions

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

'''

#solution 1
#1.分割字符串
#2.循环查找最小值
def find_short(s):
    l = s.split(' ')
    shortest = len(l[0])
    for x in l:
        if len(x) < shortest:
            shortest = len(x)
    return shortest

#solution 2
#1.循环返回长度list
#2.min()取出list中最小值
def find_short(s):
    return min([len(x) for x in s.split()])


#solution 3
#1.循环返回长度list
#2.min()取出最小值,key设置为len
def find_short(s):
    l = s.split()
    m = min(l,key=len)
    return len(m)


#solution 4
#1.循环返回长度list
#2.使用map创建长度和单词的映射
#3.min()取出最小值
def find_short(s):
    l = s.split()
    return min(map(len,l))