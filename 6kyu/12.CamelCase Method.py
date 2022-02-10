'''
12.CamelCase Method

Instructions

Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. 
All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord

'''

#solution 1
#1.使用split将string分割为word
#2.使用captitalize将每个word首字母大写
#3.使用join连接,其中的空格已经去除
def camel_case(string):
    return ''.join(s.capitalize() for s in string.split(' '))


#solution 2
#1.使用str的title方法将每个word的首字母大写
#2.使用str的replace方法将空格去除
def camel_case(string):
    return string.title().replace(' ','')