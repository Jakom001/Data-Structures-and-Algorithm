class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # create the linked list: 8->3->9->7->6
    def create_linked_list(self):
        node1 = Node(8)
        self.head = node1

        node2 = Node(3)
        node1.next = node2

        node3 = Node(9)
        node2.next = node3

        node4 = Node(7)
        node3.next = node4

        node5 = Node(6)
        node4.next = node5

    # print linked list in format: A->B->C
    def display(self):
        current = self.head

        while current:
            print(f"{current.data}", end="->")
            current = current.next
        
        print(None)

    # Delete the first node
    def delete_first_node(self):
        # if the linked_list is not empty
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data

    def delete_given_node(self, position=1):
        # if linked lis is empty
        if self.head is  None:
            return
        # Delete node at first position
        if position == 1:
            self.head = self.head.next
            return

        current = self.head
        
        # if position is greater than number of nodes
        if current.next is None:
            return

        for i in range(1, position -1):
           # if position is greater than number of nodes
           if current.next is None:
               return
           current =  current.next

        current.next = current.next.next

linked_list = LinkedList()
linked_list.create_linked_list()

print("Original List:")
linked_list.display()

print()

# delete first node
linked_list.delete_first_node()
print("After deleting first node")
linked_list.display()

print()

# delete node at position 1
linked_list.delete_given_node(2)
print("After deleting node at position 2:")
linked_list.display()

print()

# delete node at position 10
linked_list.delete_given_node(10)
print("After deleting node at position 10:")
linked_list.display()
