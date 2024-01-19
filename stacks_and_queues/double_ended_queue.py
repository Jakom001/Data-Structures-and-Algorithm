class Deque:
    def __init__(self):
        # initialize an empty deque
        self.deque = []

    # function to add element from the rear end
    def add_rear(self, item):
        self.deque.append(item)

    # function to add element from the front end
    def add_front(self, item):
        self.deque.insert(0, item)

    # function to delete  element from the front end
    def remove_front(self):
        return self.deque.pop(0)

    # function to append element from the rear end
    def remove_rear(self):
        return self.deque.pop()
        
    # function to print the queue
    def print_queue(self, message):
        print(f"{message}: {self.deque}")

d = Deque()
d.print_queue("Empty queue")
d.add_rear(8)
d.add_rear(5)
d.print_queue("After inserting from rear")
d.add_front(7)
d.add_front(10)
d.print_queue("After inserting from front")
d.remove_rear()
d.print_queue("After removing from rear")
d.remove_front()
d.print_queue("After removing from front")
