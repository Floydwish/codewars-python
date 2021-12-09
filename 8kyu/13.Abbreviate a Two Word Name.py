'''
13.Abbreviate a Two Word Name

Instructions

Write a function to convert a name into initials. This kata strictly 
takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
'''

#solution 1
#1.第1个字符 + '.' + 空格后的第1个字符，再转为大写
def abbrev_name(name):
    return (name[0]+'.'+name[name.find(' ')+1]).upper()


#solution 2
#1.将name转为大写，以' '分开，返回2个str
#2.连接结果str
def abbrev_name(name):
    first,last = name.upper().split(' ')
    return first[0]+'.'+last[0]

#solution 3
#1.将name以' '分开
#2.使用join连接
#3.转为大写
def abbrevName(name):
    return '.'.join(s[0] for s in name.split()).upper()
