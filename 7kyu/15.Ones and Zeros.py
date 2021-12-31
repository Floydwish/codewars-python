'''
15.Ones and Zeros

Instructions

Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
However, the arrays can have varying lengths, not just limited to 4.

'''

#solution 1
#1.逆序后循环列表(遍历元素)
#2.从低位到高位计算并累加
def binary_array_to_number(arr):
    ret=0
    index=0
    for x in reversed(arr):
        ret += x*pow(2,index)
        index+=1
    return ret

#solution 2
#1.逆序后循环列表(遍历序号)
#2.从低位到高位计算并累加
def binary_array_to_number(arr):
    ret=0
    index=0
    for i in range(len(arr)-1,-1,-1):
        ret += arr[i]*pow(2,index)
        index+=1
    return ret


#solution 3
#1.从高位到低位遍历元素
#2.每次计算:高位值*2+低位值
def binary_array_to_number(arr):
    ret=0
    for x in arr:
        ret=ret*2+x
    return ret


#solution 4
#1.将列表元素转为string并连接为字符串
#2.使用int函数将字符串转为int,第2个参数为2,表示进制
def binary_array_to_number(arr):
    return int(''.join(str(x) for x in arr),2)


#solution 5
#1.使用map(fun,iter)将list转为string,使用join连接为字符串
#2.使用int函数将字符串转为int,第2个参数为2,表示进制
def binary_array_to_number(arr):
    return int(''.join(map(str, arr)),2)
