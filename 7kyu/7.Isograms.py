'''
7.Isograms

Instructions

An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter casing)

'''

#solution 1:
#1.将string统一转为小写或大写
#2.循环查找，若遇到2个或以上的重复字符，返回false，循环结束，返回true
def is_isogram(string):
    s = string.lower()
    for c in s:
        if s.count(c)>1:
            return False
    return True


#solution 2:
#1.将string转为小写
#2.将全小写的string用于创建set(set中每一个元素都是唯一的，也就是没有重复元素，据此即可判断是否重复)
#3.计算set长度并与原string长度比较,比较结果即为返回结果
def is_isogram(string):
    return len(string) == len(set(string.lower()))