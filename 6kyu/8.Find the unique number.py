'''
8.Find the unique number

Instructions

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique

example:
test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)


'''

#solution 1
#1.排序,可能为第1个元素或最后一个元素
#2.比较确认结果
def find_uniq(arr):
    l=list(arr)
    l.sort()
    return l[0] if l[0]!=l[1] else l[len(l)-1]


#solution 2
#1.使用set(元素unique)
#2.使用count计算set中每个元素的数量,数量为1则为结果
def find_uniq(arr):
    se = set(arr)
    for x in se:
        if arr.count(x) == 1:
            return x


#solution 3
#1.使用set(元素unique)
#2.使用count计算set中每个元素的数量,数量为1则为结果
def find_uniq(arr):
    a,b = set(arr)
    return a if arr.count(a)==1 else b