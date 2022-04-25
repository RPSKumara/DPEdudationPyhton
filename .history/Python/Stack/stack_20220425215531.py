from multiprocessing.sharedctypes import Value


def push (stack,value):
    return stack.append(value)
def pop(stack):
    stack.pop()
myList = []
push(myList,5)
push(myList,10)
push(myList,30)
pop(myList)
print(myList)

