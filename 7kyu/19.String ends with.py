'''
19.String ends with?

Instructions

Complete the solution so that it returns true if the first argument(string) passed in ends with 
the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

'''

#solution 1
#1.切片截取出尾部字串
#2.与参数2比较,返回比较结果
def solution(string, ending):
    return string[len(string)-len(ending):] == ending

#solution 2
#0.solution 1优化
#1.切片截取出尾部字串
#2.与参数2比较,返回比较结果
def solution(string, ending):
    return string[-len(ending):] == ending


#solution 3
#1.使用string的函数endswith判断
def solution(string, ending):
    return string.endswith(ending)

#solution 4
#1.切片截取出尾部字串
#2.使用in判断参数2是否包含在尾部字串中
def solution(string, ending):
    return ending in string[-len(ending):]