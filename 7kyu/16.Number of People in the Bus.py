'''
16.Number of People in the Bus

Instructions

There is a bus moving in the city, and it takes and drop some people in each bus stop.

You are provided with a list (or array) of integer pairs. 
Elements of each pair represent number of people get into bus (The first item) and 
number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus 
station (after the last array). Even though it is the last bus stop, the bus is not empty and 
some people are still in the bus, and they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. 
So the return integer can't be negative.

The second value in the first integer array is 0, since the bus is empty in the first bus stop.

'''

#solution 1
#1.循环遍历list
#2.累加上车人次和下车人次,返回差值,即为最后一站剩下的人数
def number(bus_stops):
    upCount, downCount = 0 
    for up,down in bus_stops:
        upCount+=up
        downCount+=down
    return upCount-downCount


#solution 2
#1.循环遍历list
#2.累加上车人次和下车人次的差值,结果即为最后一站剩下的人数
def number(bus_stops):
    count = 0
    for up,down in bus_stops:
        count+=up-down
    return count


#solution 3
#1.循环遍历list
#2.sum累加每站上车人次和下车人次的差值
def number(bus_stops):
    return sum(up-down for up,down in bus_stops)