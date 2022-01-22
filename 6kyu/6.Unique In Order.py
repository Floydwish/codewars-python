'''
6.Unique In Order

Instructions

Past Solutions
Implement the function unique_in_order which takes as argument a sequence and 
returns a list of items without any elements with the same value next to each other and 
preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

'''

#solution 1
#1.处理元素数量为0或1的特殊情况
#2.循环前后比较，若不同则放置到结果list中
def unique_in_order(iterable):
    if(len(iterable)==0):
        return []
    if(len(iterable)==1):
        return list(iterable)
    l=list(iterable)
    ll = list()
   
    ll.append(l[0])
    for index in range(1,len(l)):
        if l[index-1] != l[index]:
            ll.append(l[index])
            
    return ll


#solution 2
#0.solution 1优化
#1.处理元素数量为0或1的特殊情况
#2.循环前后比较，若不同则放置到结果list中(原list角度)
def unique_in_order(iterable):
    ret = []
    pre = None
    for x in iterable:
        if pre != x:
            ret.append(x)
        pre = x
    return ret


#solution 3
#1.处理元素数量为0或1的特殊情况
#2.循环遍历，将循环当前元素与结果list中最后一个元素进行比较(结果list的角度)
def unique_in_order(iterable):
    ret = []
    for x in iterable:
        if len(ret)==0 or x != ret[-1]
            ret.append(x)
    return ret