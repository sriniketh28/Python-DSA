class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def add_at_middle(self, prev_node, data):
        if prev_node is None:
            print("Previous node should be given")
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        new_node.next = None
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def getCount(self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        print(count)    
    
    def delete(self, data):
        temp = self.head
        if temp is None:
            print("Linked List does not exist")

        if temp.data == data:
            self.head = temp.next
            temp = None
            return

        while(temp):
            if temp.data == data:
                break
            prev_node = temp
            temp = temp.next

        if temp == None:
            print("The data value given is not in Linked List")
            return

        prev_node.next = temp.next
        temp = None
        
if __name__ == "__main__":
    lList = LinkedList()
    lList.head = Node(1)
    second = Node(2)
    third = Node(3)

    lList.head.next = second
    second.next = third

    lList.add_at_end(4)

    lList.delete(5)

    lList.printLinkedList()

