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
    number=n*n
    push(squareNumbers,number)
    print(number)
    n+=1
print(squareNumbers)

# myList = []
# push(myList,5)
# print(myList)
# pop(myList)
# print(myList)

