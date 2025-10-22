class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class Queue:
    def _init_(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node  # ✅ Fix: update both front & rear
            return
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
print(q.dequeue())
print(q.dequeue())
