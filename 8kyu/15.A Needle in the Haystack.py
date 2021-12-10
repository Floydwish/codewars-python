'''
15.A Needle in the Haystack

Instructions

Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])

'''

#solution 1
#1.使用list的index函数
#2.若找到，则返回位置
#3.使用format格式化输出
def find_needle(haystack):
    try:
        ind = haystack.index('needle')
        if ind>=0:
            return ('found the needle at position {}'.format(ind))
    except:
        return "not find"


#solution 2
#solution 1简化
#1.使用list的index函数
#2.若找到，则返回位置
def find_needle(haystack):
    return ('found the needle at position {}'.format(haystack.index('needle')))


#solution 3
#1.使用list的index函数
#2.若找到，则返回位置
#3.使用 %d 格式化
def find_needle(haystack):
    return 'found the needle at position %d' % haystack.index('needle')

#solution 4
#1.使用list的index函数
#2.若找到，则返回位置
#3.连接结果字符串
def find_needle(haystack):
    return 'found the needle at position ' + str(haystack.index('needle'))

                    
