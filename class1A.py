import math
import random

#生成7-9加其它数，结果在10到20之间的算式


problems = []
for i in range(1, 10):
	for j in range(1, 10):
                #if(i + j > 10):
                problems.append("{0}+{1}=".format(i, j))

col = 0;
line = ''
span = "\t"
lenth = len(problems)

def getRandomChar(str1):
    pos = math.floor(random.random()*len(str1));
    return str1[pos];

def paddingWithSpace(str1, length):
    while(len(str1) < length):
        equation += " ";

def getTitle():
    first = int(math.ceil(random.random()*10));
    second = int(math.ceil(random.random()*10));
    third = int(math.ceil(random.random()*10));
    op1 = getRandomChar("+-");
    op2 = getRandomChar("+-");
    equation = "{0}{1}{2}{3}{4}".format(first, op1, second, op2, third);
    if(int(eval(equation)) < 0):
        return getTitle();
    else:
        equation+="=";
        return equation.ljust(12, ' ');

print("写出得数");
for i in range(0, 200):
    line = line + getTitle() + span
    col += 1
    if(col % 5 == 0):
        print(line)
        line = ""
		
print("在()中填写合适的数，使等式成立");
for i in range(0, 200):
    first = int(math.ceil(random.random()*10));
    second = first + int(math.ceil(random.random()*10));
    equation = "{0}+(  )={1}".format(first, second).ljust(12, ' ');
    line = line + equation + span
    col += 1
    if(col % 5 == 0):
        print(line)
        line = ""

def getTitle1():
    first = int(math.ceil(random.random()*10));
    second = int(math.ceil(random.random()*10));
    op1 = getRandomChar("+-");
    equation = "{0}{1}{2}".format(first, op1, second);
    if(int(eval(equation)) < 1):
        return getTitle1();
    else:
        return equation;

print("在()中填写+ - =");
for i in range(0, 200):
    eq = getTitle1();
    op2 = getRandomChar("+-");
    diff = getRandomChar("012");
    result = int(eval(eq+op2+diff));
    equation = "{0}(  ){1}".format(eq, second).ljust(12, ' ');
    line = line + equation + span
    col += 1
    if(col % 5 == 0):
        print(line)
        line = ""

