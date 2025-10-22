class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = new_node
            return  # ❌ Missing update for rear pointer
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Empty"
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  # Expected 10
print(q.dequeue())  # Expected 20
