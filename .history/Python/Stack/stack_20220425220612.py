from multiprocessing.sharedctypes import Value
import numbers
from tkinter import N


def push (stack,value):
    return stack.append(value)
def pop(stack):
    stack.pop()

squareNumbers = []
n=0
while(n<100):
    n+=1
    numberText = str(n) + " * "+ str(n) + " = " + str(n*n) + "\n"
    push(squareNumbers,numberText)
    print(numberText)
print(squareNumbers)

# myList = []
# push(myList,5)
# print(myList)
# pop(myList)
# print(myList)

