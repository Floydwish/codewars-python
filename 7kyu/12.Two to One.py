'''
12.Two to One

Instructions

Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, the longest possible, containing distinct letters - 
each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''

#solution 1
#1.连接2个string
#2.将string添加到集合set(无序,不重复元素序列,用于去重)
#3.排序
#4.添加到字符串
def longest(a1, a2):
    return ''.join(sorted(set(a1+a2)))


#solution 2
#1.创建字母表
#2.连接2个string
#3.循环遍历字母表,元素在合并的sting能找到则放置到结果string, 否则继续

#注：
#1.该方式根据现成的字母表顺序,保证顺序
#2.字母表遍历,保证只添加一次
def longest(a1, a2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = a1+a2
    ret = ''

    for x in alphabet:
        if x not in s:
            continue
        else:
            ret += x
    return ret


