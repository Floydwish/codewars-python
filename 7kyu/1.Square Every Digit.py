'''
1.Square Every Digit

Instructions

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

Note: The function accepts an integer and returns an integer

'''

#solution 1
def square_digits(num):
    retStr=""
    numStr = str(num)
    for c in numStr:
        retStr += str(int(c)*int(c))
    return int(retStr)


#solution 2
#1.在solution 1基础上，将平方计算换为n**2方式
def square_digits(num):
    ret=""
    for c in str(num):
        ret += str(int(c)**2)
    return int(ret)


#solution 3
#1.将num转为str
#2.使用循环取字符，将字符转为数字，计算平方，再转为str
#3.使用join连接循环计算出的每个str
#4.将连接后的str转为int
def square_digits(num):
    return int(''.join(str(int(c)**2) for c in str(num)))
