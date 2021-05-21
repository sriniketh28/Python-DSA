from collections import deque

class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    
    def isEmpty(self):
        return True if len(self.queue2)==0 else False

    def push(self, data):
        self.queue1.append(data)
        while self.queue2:
            temp = self.queue2.popleft()
            self.queue1.append(temp)
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.queue2:
            return self.queue2.popleft()
        return -1

stack1 = Stack()
print(stack1.pop())
print(stack1.isEmpty())
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
print(stack1.pop())
print(stack1.isEmpty())
