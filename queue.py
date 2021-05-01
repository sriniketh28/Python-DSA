from collections import deque

# list.pop(0) takes O(n)

# list. pop(0) removes the first element. 
# All remaining elements have to be shifted up one step, so that takes O(n) linear time.

# deque.popleft() takes O(1)

# Queue can have a dynamic or fixed size.

class Queue:
    def __init__(self):
        self.queue = deque([])

    def isEmpty(self):
        if(len(self.queue) == 0):
            return True
        else:
            return False
        
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue.popleft()

    def front(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue[len(self.queue)-1]

    def rear(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue[0]

    def printQueue(self):
        print(self.queue)

    def queueSize(self):
        return len(self.queue)

queue1 = Queue()
queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)
queue1.enqueue(40)
queue1.enqueue(50)
queue1.printQueue()
queue1.dequeue()
queue1.printQueue()
print(queue1.front())
print(queue1.rear())
print(queue1.queueSize())

