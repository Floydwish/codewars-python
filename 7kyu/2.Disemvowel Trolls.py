'''
2.Disemvowel Trolls

Instructions

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, 
neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
'''

#solution 1
def disemvowel(s):
    result = s
    for c in result:
        if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
            result = result.replace(c,'')
    return result


#solution 2
#1.循环替换s中的元音字符
def disemvowel(s):
    for c in 'aeiouAEIOU':
        s = s.replace(c,'')
    return s

#solution 3
#1.循环遍历s,将不属于元音字母的字符筛选出来
#2.使用join连接字符
def disemvowel(s):
    return ''.join(c for c in s if c.lower() not in "aeiou")
