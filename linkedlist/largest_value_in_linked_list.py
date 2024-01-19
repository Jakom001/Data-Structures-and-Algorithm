class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # method to return the largest number 
    def find_largest(self):
        # condition to handle empty linked list
        if not self.head:
            return None
        current = self.head
        # initialize the value of head as largest
        largest = current.data
        # iterate until the last node
        while current:
            # update largest if necessary
            if current.data > largest:
                largest = current.data
            current = current.next
        return largest

# create a linked list
linked_list = LinkedList()

# add five nodes
linked_list.append(85)
linked_list.append(90)
linked_list.append(78)
linked_list.append(92)
linked_list.append(88)

largest = linked_list.find_largest()
print(f'Largest value: {largest}')
