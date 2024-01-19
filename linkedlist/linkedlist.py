# Create singly linked list
# Linked list operations insert, delete

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    # Create linked list
    def create_linked_list(self):
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)
        node4 = Node(40)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
    
    # Traverse / Display linked list
    def traverse_linked_list(self):
        current = self.head

        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)
    
    def count_elements(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def insert_at_beginning(self, data):
        new_node =  Node(data)

        # if the linked list is empty
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head

        self.head = new_node

    def insert_at_given_position(self, data, position = 1):
        # Handle invalid positions
        if position < 1 or position > self.count_elements():
            print("Position Invalid")
            return

        # Handle insertion at beginning
        if position ==1:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        
        current = self.head

        for i in range(1, position-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def append(self, data):

        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        
        while current.next:
            current = current.next
        current.next = new_node



linkedlist = LinkedList()
linkedlist.create_linked_list()

print("Original Linked List:")
linkedlist.traverse_linked_list()
linkedlist.insert_at_beginning(100)
linkedlist.insert_at_given_position(110, 1)
linkedlist.append(120)

print("After operations")
linkedlist.traverse_linked_list()
