'''
17.Find the divisors!

Instructions

Create a function named divisors/Divisors that takes an integer n > 1 and 
returns an array with all of the integer's divisors(except for 1 and the number itself), 
from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) 
(use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"

'''

#solution 1
#1.循环遍历,限定范围,逐个取余
#2.构造输出
def divisors(integer):
    l=list()
    for i in range(2,integer):
        if integer%i == 0:
            l.append(i)
    return "{} {}".format(integer,"is prime") if len(l)==0 else l


#solution 2
#1.循环遍历,限定范围,逐个取余
#2.构造输出
def divisors(integer):
    l = [i for i in range(2,integer) if integer%i == 0]
    return str(integer)+" is prime" if len(l)==0 else l


#solution 3
#1.循环遍历,限定范围,逐个取余
#2.构造输出
def divisors(integer):
    l = [i for i in range(2,integer) if integer%i == 0]
    return l or str(integer) + " is prime"
