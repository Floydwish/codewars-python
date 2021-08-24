#1.Grasshopper - Summation

# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# For example:

# summation(2) -> 3
# 1 + 2

# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

# solution1
# using loop
def summation(num):
    sum=0
    while (num>0):
        sum+=num
        num-=1
    return sum


# solution2
# using math principle
def summation(num):
    return (num+1)*num/2


# solution3
# using built-in function
def summation(num):
    return sum(range(1,num+1))
    