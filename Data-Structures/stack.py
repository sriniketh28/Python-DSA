# Stack can have a dynamic or fixed size.

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.stack[len(self.stack)-1]

    def printStack(self):
        print(self.stack)
        
    def stackSize(self):
        print(len(self.stack))

stack1 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)

stack2 = Stack()
stack2.push(50)
stack2.push(60)
stack2.push(70)
stack2.push(80)

stack1.printStack()
stack1.pop()
stack1.printStack()
print(stack1.isEmpty())
print(stack2.peek())
stack2.printStack()
stack1.stackSize()
