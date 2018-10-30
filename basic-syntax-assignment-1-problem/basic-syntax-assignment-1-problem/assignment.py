#1 Create two variables – one with your name and one with your age
#2 Create a function which prints your data as one string
#3 Create a function which prints ANY data (two arguments) as one string
#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
import math

name = 'Henrique'
age = 50

def print_date_inline():
    print(name + ' ' + str(age))

def print_date_inline_with_params(name, age):
    print(name + ' ' + str(age))

def decades_alive(age):
    return str(math.floor(age / 10) * 1)

print_date_inline()
print_date_inline_with_params('Janny', 27)
print('You\'ve been living for ' + decades_alive(age) + ' decade(s)')
