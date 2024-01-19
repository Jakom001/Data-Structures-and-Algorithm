class Queues:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not queue1.is_empty():
            self.queue.pop(0)

    def peek(self):
        if not queue1.is_empty():
            return self.queue[0]

    def print_queue(self, message):
        print(f"{message} : {self.queue}")

queue1 = Queues()

queue1.enqueue(10)
queue1.enqueue(20)
queue1. enqueue(30)

queue1.print_queue("After adding elements to the queue")

queue1.dequeue()
queue1.print_queue("After removing first item")
queue1.dequeue()
queue1.print_queue("After removing an item")
