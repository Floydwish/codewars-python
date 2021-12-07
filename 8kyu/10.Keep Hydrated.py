'''
10.Keep Hydrated!

Instructions

Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, 
he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, 
rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5

'''

#solution 1
#1.每小时0.5 * 小时数
#2.转成整数
def litres(time):
    return int(time*0.5)


#solution 2
#1.使用地板除，只留下整数
def litres(time):
    return time//2