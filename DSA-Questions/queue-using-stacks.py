class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def isEmpty(self):
        return True if len(self.stack2)==0 and len(self.stack1)==0 else False

    def enQueue(self, data):
        self.stack1.append(data)

    def deQueue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


queue1 = Queue()
queue1.enQueue(10)
queue1.enQueue(20)
queue1.enQueue(30)
queue1.enQueue(40)
print(queue1.deQueue())
print(queue1.isEmpty())
