'''
3.Even or Odd

Instructions
Output
Create a function that takes an integer as an argument and 
returns "Even" for even numbers or "Odd" for odd numbers.
'''

#solution 1
def even_or_odd(number):
    if number%2 == 0:
        return 'Even'
    else:
        return 'Odd'


#solution 2
#1.使用三元运算符，类似C++的 (? :)
def even_or_odd(number):
    return 'Even' if number%2 == 0 else 'Odd'


'''
solution 2 note:

After a long discussion I've decided to add a shortcut conditional
expression to Python 2.5.

The syntax will be

    A if C else B

This first evaluates C; if it is true, A is evaluated to give the
result, otherwise, B is evaluated to give the result.

The priorities will be such that you can write

    x = A if C else B
    x = lambda: A if C else B
    x = A if C else B if D else E

url:https://mail.python.org/pipermail/python-dev/2005-September/056846.html
'''