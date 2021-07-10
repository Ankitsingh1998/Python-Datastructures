#Data structure - Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()  
    #index inside pop/dequeue will be nothing or (-1) to remove last element

    def print_queue(self):
        print(self.items)

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('42')
q.print_queue()
print(q.dequeue())
q.print_queue()
print(q.is_empty())

"""
Queue --> like persons in queue for ice-cream.
First In, First Out --> FIFO, Fist one that was buying ice-cream in a
queue will exit the line first. First item that was inserted in the 
beginning will be removed first.
Here, itema will store our elements.
enqueue --> inserts/adds an item at first place.
dequeue --> removes an item from last position.
"""
"""
Applications:
    --> are used whenever we need to manage objects in order starting
    with the first one in, printing documents on a printer, call center
    systems to answering people on hold, and so on.
"""