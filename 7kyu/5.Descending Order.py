'''
5.Descending Order

Instructions

Your task is to make a function that can take any non-negative integer as an argument and 
return it with its digits in descending order. Essentially, rearrange the digits to 
create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

'''

#solution 1
#0.转换 -> 排序 -> 转换
#1.将interger转为string, 再转为list
#2.使用list的sort排序，逆序(该sort为list方法)
#3.list转为string,转为int返回
def descending_order(num):
    l=list(str(num))
    l.sort(reverse=True)
    ret=''.join(l)
    return int(ret)

#solution 2
#0.转换 -> 排序 -> 转换
#1.interger转为string
#2.使用sorted排序该string,逆序(sorted为针对所有可迭代对象的方法)
#3.结果为list,转为string,转为int返回
def descending_order(num):
    return int(''.join(sorted(str(num),reverse = True)))



