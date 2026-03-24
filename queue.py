class Queue():
    def __init__(self,size):
        self.list = [None] * size
        self.maximum = size
        self.front = 0
        self.rear = -1
        self.available = size
    def enqueue(self,item):
        if self.available > 0:
            self.rear += 1
            self.list[self.rear] = item
            self.available -= 1
        else:
            print("Unable to add item; queue is full")
    def dequeue(self):
        if self.available == self.maximum:
            print("Queue was already empty, unable to delete an item")
        else:
            self.list[self.front] = None
            self.front += 1
            self.available += 1
    def display(self):
        for i in self.list:
            print(i)
    def printfront(self):
        print(self.list[self.front])
    def printrear(self):
        print(self.list[self.rear])


object = Queue(3)
object.enqueue(4)
object.enqueue(5)
object.enqueue(6)
object.enqueue(7)
object.display()
object.dequeue()
object.dequeue()
object.display()
object.printfront()
object.printrear()
