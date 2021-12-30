'''
14.Categorize New Member

Instructions

The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
They would like your help with an application form that will tell prospective members 
which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. 
Information consists of an integer for the person's age and an integer for the person's handicap.

Output
Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the 
respective member is to be placed in the senior or open category.

Example
input =  [(18, 20), (45, 2), (61, 12), (37, 6), (21, 21), (78, 9)]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

'''

#solution 1
#1.创建空list
#2.循环入参list中的元祖
#3.取出元祖中的数据进行比较,根据比较结果填入相应值
def open_or_senior(data):
    l=list()
    for t in data:
        if t[0]>=55 and t[1]>7:
            l.append("Senior")
        else:
            l.append("Open")
    return l


#solution 2
#solution 1
#1.创建空list
#2.循环取出入参list中的元祖值
#3.比较,填入值
def open_or_senior(data):
    l=list()
    for age,handicap in data:
        if age>=55 and handicap>7:
            l.append("Senior")
        else:
            l.append("Open")
    return l

#solution 3
#1.solution 2一行优化版
def open_or_senior(data):
    return ["Senior" if age>=55 and handicap>7 else "Open" for (age,handicap) in data]