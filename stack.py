def createStack():
    stack = []
    return stack

def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def push(stack, data):
    stack.append(data)

def pop(stack):
    if isEmpty(stack):
        return "Stack is Empty"
    else:
        return stack.pop()

def peek(stack):
    if isEmpty(stack):
        return "Stack is Empty"
    else:
        return stack[len(stack)-1]

def printStack(stack):
    print(stack)

stack1 = createStack()
push(stack1, 10)
push(stack1, 20) 
push(stack1, 30)
push(stack1, 40)

stack2 = createStack()
push(stack2, 50)
push(stack2, 60) 
push(stack2, 70)
push(stack2, 80)

printStack(stack1)
pop(stack1)
printStack(stack1)
printStack(stack2)
print(peek(stack1))
print(peek(stack2))

