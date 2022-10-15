'''Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный.
*Пример:* 
2+2 => 4; 
1+2*3 => 7; 
1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций.
    *Пример:* 
    1+2*3 => 7; 
    (1+2)*3 => 9;'''

import math
import os
clear = lambda: os.system('clear')
clear()

print("Калькулятор усовершенствованный")

import re

test_str = input("Введите пример: ")

# print(test_str.find('('))


def split(s):
    return [char for char in s]

def coordinates(a, b, c):
    if (b == "/" or b == "mod" or b == "div") and c == 0:
        print("Деление на 0!")
    elif b == "*":
        w=a*c
        # print (a*c)
    # elif b == "mod" and b!=0:
    #     w=a % c
    #     print(a % c)
    elif b == "+":
        w=a+c
        # print(a+c)
    elif b == "-":
        w=a-c
        # print(a-c)
    # elif b == "pow":
    #     w=a**c
    #     print(a ** c)
    # elif b == "div" and b!=0:
    #     w=a//c
    #     print(a // c)
    elif b == "/" and b!=0:
        w=a/c
        # print(a/c)
    return w


if test_str.find('(')>=0:
    res = re.findall(r'\(.*?\)', test_str)
    # print("res", res)

    z=res[0].replace("(", "")
    z=z.replace(")", "")

    # print("z", z)
    x=split(z)
    r=coordinates(int(x[0]), x[1], int(x[2]))

    a = test_str.replace(res[0], str(r))
    # print("a", a)

    s=split(a)
    print(f"\n{test_str} => {coordinates(int(s[0]), s[1], int(s[2]))}\n")
else:
    s=split(test_str)
    print(f"\n{test_str} => {coordinates(int(s[0]), s[1], int(s[2]))}\n")