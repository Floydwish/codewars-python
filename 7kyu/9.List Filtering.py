'''
9.List Filtering

Instructions

In this kata you will create a function that takes a list of non-negative integers and 
strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

'''

'''
solution 1
1.循环取出list元素
2.使用isinstance()判断元素类型
3.当类型为int时,放置到结果list中
'''
def filter_list(l):
  ret = list()
  for x in l:
    if isinstance(x,int):
        ret.append(x)
  return ret


'''solution 2
1.使用单行循环筛选并创建新列表
2.使用isinstance()筛选int类型
'''
def filter_list(l):
    return [x for x in l if isinstance(x,int)]


'''solution 3
1.使用单行循环筛选并创建新列表
2.使用type()筛选int类型
'''
def filter_list(l):
    return [x for x in l if type(x) is int]