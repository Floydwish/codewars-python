'''
13.Find the next perfect square!

Instructions

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square 
after the one passed as a parameter. Recall that an integral perfect square is 
an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. 
You may assume the parameter is non-negative.

Examples:(Input --> Output)

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square

'''

'''
solution 1
1.计算入参的开方值,并取整(内置pow)
2.将开方值再平方,与入参比较是否相等
3.相等则判断符合要求,加1后再开平方返回;否则返回-1
'''
def find_next_square(sq):
    m = int(pow(sq,0.5))
    if pow(m,2) != sq:
        return -1
    else:
        return pow(m+1,2)


'''
solution 2
1.计算入参的开方值(连乘 '**')
2.得到值为float,使用is_integer()判断是否为整数
3.是整数则加1后开平方返回,否则返回-1
'''
def find_next_square(sq):
    m = sq ** 0.5
    if m.is_integer():
        return (m+1)**2
    return -1


'''
solution 3
1.计算入参的开方值(连乘 '**')
2.得到值为float,使用%1,根据余数判断是否为整数
3.是整数则加1后开平方返回,否则返回-1
'''
def find_next_square(sq):
    m = sq ** 0.5
    return -1 if m%1 else (m+1)**2