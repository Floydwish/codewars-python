'''
14.Convert number to reversed array of digits

Instructions

Convert number to reversed array of digits

Given a random non-negative number, you have to return the digits of this number 
within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
0 => [0]

'''

#solution 1
#1.数字转为string
#2.string转为list
#3.list进行反转
#4.list[str]转为list[int]
def digitize(n):
    s=str(n)
    l=list(s)
    l.reverse()
    return list(map(int,l))


#solution 2
#1.数字转为string,使用slice反转
#2.循环将str转为int
#3.循环放在[]中，作为List返回
def digitize(n):
    return [int(x) for x in str(n)[::-1]]


#solution 3
#1.数字转为string,使用slice反转
#2.使用map转为int
#3.结果作为list返回
def digitize():
    return list(map(int,str(n)[::-1]))
