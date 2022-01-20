'''
5.Your order please

Instructions

Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only 
contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""


test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
test.assert_equals(order(""), "")

'''

#solution 1
#1.双循环
#2.将给定字符串分割成列表
#3.从列表中查找数字,符合条件的就把string放置到结果字串
#4.返回截取后的结果
def order(sentence):
    ret=''
    l = sentence.split(' ')
    for i in range(1,10):
        for s in l:
            if s.find(str(i)) != -1:
                ret += s+' '
                break                

    return ret[:len(ret)-1]


#solution 2
#1.双循环
#2.将给定字符串分割成列表
#3.从列表中查找数字,符合条件的添加到结果list
#4.连接结果list后返回
def order(sentence):
    ret = list()
    l = sentence.split(' ');
    for i in range(1,10):
        for s in l:
            if s.find(str(i)) != -1:
                ret.append(s)
                break
    return ' '.join(ret)


#solution 3
#1.将sentence分割为list
#2.排序该list,排序的key为每一个list元素的单独排序后结果(单个元素排序后数字在前,以此排序)
#3.排序后的list连接为结果string
def order(sentence):
    l = sentence.split()
    ret = sorted(l, key = lambda s:sorted(s))
    return ' '.join(ret)



#solution 4
#1.增加独立的提取word中数字的接口
#2.将sentence分割成word
#3.使用sorted排序列表,key为每个word中提取出来的数字
#4.使用空格连接排序后的list作为结果
def extract_number(word):
    for x in word:
        if x.isdigit():
            return int(x)
    return None

def order(sentence):
    l = sentence.split()
    ret = sorted(l, key=extract_number)
    return ' '.join(ret)

