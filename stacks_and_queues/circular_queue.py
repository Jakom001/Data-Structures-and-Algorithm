# create class to represent a circular queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        # initialize front pointer
        self.front = 0 
        # count the number of elements in the queue
        self.count = 0 

    # check if the queue is full
    def is_full(self):
        return self.count == self.size

    # check if the queue is empty
    def is_empty(self):
        return self.count == 0

    # if queue is not full, perform enqueue and increment count
    def enqueue(self, item):
        if self.is_full():
            return
        index = (self.front + self.count) % self.size
        self.queue[index] = item
        self.count += 1

    # if queue is not empty, perform dequeue and decrement count
    def dequeue(self):
        if self.is_empty():
            return
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1

    def print_queue(self, message):
        print(f"{message}: {self.queue}")

# initialize circular queue with size 4
queue1 = CircularQueue(4)

# enqueue operations
queue1.enqueue(5)
queue1.enqueue(10)
queue1.enqueue(100)
queue1.print_queue("Queue after adding 3 elements")

# dequeue operation
queue1.dequeue()
queue1.print_queue("After removing an item")

# enqueue operations
queue1.enqueue(150)
queue1.enqueue(200)
queue1.print_queue("After adding two more items")

# trying to enqueue when queue is full
queue1.enqueue(250)
