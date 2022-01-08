'''
20.Reverse words

Instructions

Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

'''

#solution 1
#1.分割字串,获取字串
#2.翻转字串
#3.连接字串
def reverse_words(text):
  l=text.split(' ')
  lret=list()
  for x in l:
    lret.append(x[::-1])
  return ' '.join(lret)


#solution 2
#1.分割字串,获取字串
#2.翻转字串
#3.连接字串
def reverse_words(text):
    return ' '.join(s[::-1] for s in text.split(' '))