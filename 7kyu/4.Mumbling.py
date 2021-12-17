'''
4.Mumbling

Instructions

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

'''

#solution 1
#1.循环取字符，并记下当前字符的序号
#2.序号每次循环+1,并在结果字符串后面添加：当前字符*序号+'-'
#3.调用string的title接口，将每个词首字母大写
#4.使用[:-1]切片去除最后一个'-'
def accum(s):
    cont=0
    ret=''
    for c in s:
        cont+=1
        ret += c*cont + '-'
    return ret.title()[:-1]

#solution 2
#solution 1 的优化
#1.循环取字符
#2.结果字符串后面添加：当前字符*(序号+1)+'-'
#3.调用string的title接口，将每个词首字母大写
#4.使用[:-1]切片去除最后一个'-'
def accum(s):
    ret=''
    for i in range(len(s)):
        ret += s[i] * (i+1) + '-'
    return ret.title()[:-1]

#solution 3
#1.使用enumerate创建出字符下标和字符的序列(下标从0开始)
#2.循环该序列，同时将字符和下标提取出来，做相应处理：第1个字符大写，后续字符小写，小写字符数等于下标值
#3.使用'-'连接起来
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


#solution 4
#1.使用enumerate创建出字符下标和字符的序列(下标从1开始)
#2.循环该序列,每次循环得到指定数量的小写字符,调用title()让首字母大写
#3.使用'-'连接
def accum(s):
    return '-'.join((c*i).title() for i, c in enumerate(s,1))



