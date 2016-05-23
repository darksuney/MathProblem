# -*- coding: cp936 -*-
import math
import random

#生成两位数加一位数，结果会进位的加法算式

span= '    ';

def getRandomChar(str1):
    pos = int(math.floor(random.random()*len(str1)));
    return str1[pos];

def paddingWithSpace(str1, length):
    while(len(str1) < length):
        equation += " ";

def getTitle():
    first = 10 + int(math.ceil(random.random()*90));
    second = int(math.ceil(random.random()*10));
    op1 = '+';
    equation = "{0} {1} {2}".format(first, op1, second);

    excepted = first - (first % 10) + 10;
    if(int(eval(equation)) < excepted):
        return getTitle();
    else:
        equation+="=";
        return equation.ljust(12, ' ');


def printTitle(number):
        col = 0;
        line = ''
        print("写出得数");
        for i in range(0, number):
            line = line + getTitle() + span
            col += 1
            if(col % 5 == 0):
                print(line)
                line = ""

for i in range(0,5):
    printTitle(50)
