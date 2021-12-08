'''
12.Basic Mathematical Operations

Instructions

Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7

'''

#solution 1
#1.条件判断
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1+value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1*value2
    elif operator == '/':
        return value1/value2


#solution 2
#1.使用eval
#2.将操作数转为str，连接字符串，调用eval计算
def basic_op(operator, value1, value2):
    eval(str(value1) + operator + str(value2))

#solution 3
#1.使用eval
#2.使用str的format接口对操作数和操作符进行格式化，得到str,调用eval计算
def basic_op(operator, value1, value2):
    return eval('{}{}{}'.format(value1,operator,value2))
