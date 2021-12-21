'''
6.Get the Middle Character

Instructions

You are going to be given a word. Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. If the word's length is even, 
return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"

#Input

A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 
in some test cases due to an error in the test cases). You do not need to test for this. 
This is only here to tell you that you do not need to worry about your solution timing out.

#Output

The middle character(s) of the word represented as a string.

'''

def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]

#solution 1
#1.字符串连接
def get_middle(s):
    l=len(s)
    return str(s[l//2]) if l%2==1 else str(s[l//2-1]) + str(s[l//2])


#solution 2
#1.字符串切片
def get_middle(s):
    l=len(s)
    return (s[l//2:l//2+1]) if l%2==1 else s[l//2-1:l//2+1]


#solution 3
#1.调用divmod返回商和余数，作为中间值下标，以及是否为奇数的判断依据
#注：returns a tuple containing the quotient  and the remainder 
def get_middle(s):
    index, odd = divomd(len(s),2)
    return s[index] if odd==1 else s[index-1:index+1]

#solution 4
#数学方式
#1.l为奇数时,(l-1)//2 等于 l//2, 与l//2+1组合进行切片，即为取中间值 
#2.l为偶数时，(l-1)//2 等于 l//2 -1, 与l//2+1组合进行切片，即为取2个中间值
def get_middle(s):
    l=len(s)
    return s[(l-1)//2:l//2+1]