'''
3.Highest and Lowest

Instructions

In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.

'''

#solution 1
#1.处理特殊情况
#2.将字符串分割为单个字符
#3.循环比较字符转数字的大小，挑选出最大和最小值
def high_and_low(numbers):
    if len(numbers) == 1:
        return str(numbers) + ' ' + str(numbers)
    l = numbers.split(' ')
    minNum=int(l[0])
    maxNum=int(l[0])
    for x in l:
        if int(x) > maxNum:
            maxNum = int(x)
        elif int(x) < minNum:
            minNum = int(x)
    return str(maxNum) + ' ' + str(minNum)


#solution 2
#1.将字符串分割为字符，并转为包含int数值的列表
#2.利用max和min分别计算最大值和最小值，使用string的格式化返回结果
def high_and_low(numbers):
    nm = [int(x) for x in numbers.split(' ')]
    return '%d %d' % (max(nm),min(nm))


#solution 3
#1.将字符串分割为字符，并转为包含int数值的列表
#2.利用max和min分别计算最大值和最小值，使用string的格式化返回结果
# 注：关于格式化-https://pyformat.info
def high_and_low(numbers):
    nm = [int(x) for x in numbers.split(' ')]
    return '{} {}'.format(max(nm),min(nm))



#solution 4
#1.将字符串分割为字符，并转为包含int数值的列表
#2.利用max和min分别计算最大值和最小值，连接最大、最小值
def high_and_low(numbers):
    nm = [int(x) for x in numbers.split(' ')]
    return str(max(nm)) + ' ' + str(min(nm))

