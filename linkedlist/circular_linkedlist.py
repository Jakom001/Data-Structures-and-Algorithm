class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a Circular Linked List class
class Circular_linkedlist:
    def __init__(self):
        self.head = None


    # Add an is_empty() method
    def is_empty(self):
        return self.head is None


    def create_linked_list(self):
        node1 = Node(20)
        node2 = Node(30)
        node3 = Node(40)
        node4 = Node(50)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4

        node4.next = self.head

    def traverse_linkedlist(self):
        if self.is_empty():
            print('Empty Linked List')
            return

        current = self.head

        while current.next != self.head:
            print(f"{current.data} -> ", end="")
            current = current.next

        print(f"{current.data} -> ", f"{self.head.data}")
    
    def count_node(self):
        if self.is_empty():
            print('Empty Linked List')
            return

        count = 1
        current = self.head

        while current.next != self.head:
            count += 1 
            current = current.next

        return count
    
    def append_into_empty(self, data):
        new_node = Node(data)
        self.head = new_node
        new_node.next = self.head


    def  append(self, data):
        if self.is_empty():
            self.append_into_empty(data)
            return

        new_node = Node(data)

        current = self.head

        while current.next is not self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head


    def insert_at_beginning(self, data):
        # if empty
        if self.is_empty():
           self.append_into_empty(data)
           return 
       
        new_node = Node(data)

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_given_position(self, data, position=1):
        if position < 1 or position > self.count_node() + 1:
            print("Invalid position to insert")
            return

        elif position==1:
            self.insert_at_beginning(data)
            return

        elif position == self.count_node()+1:
            self.append(data)
            return
        else:
            new_node= Node(data)
            current = self.head

            for i in range(1, position-1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node

    # delete from beginning
    def delete_from_beginning(self):
        if self.is_empty():
            print('Cannot delete from Empty List')
        elif self.count_node() == 1:
            temp = self.head
            self.head = None
            del temp
        else:
            temp = self.head
            current = self.head
            while current.next is not self.head:
                current = current.next
            self.head = self.head.next
            current.next = self.head
            del temp

    def delete_at_position(self, position):
        if self.is_empty():
            print('Cannot delete from Empty circular linked list')
        elif position <= 0 or position > self.count_node():
            print('Invalid position')
        elif position == 1:
            self.delete_from_beginning()
        else:
            current = self.head
            prev_node = None
            for i in range(1, position):
                prev_node = current
                current = current.next
            prev_node.next = current.next
            del current
        
linkedlist = Circular_linkedlist()
linkedlist.create_linked_list()
linkedlist.traverse_linkedlist()
linkedlist.append(160)
linkedlist.append(5)
linkedlist.insert_at_beginning(90)
linkedlist.insert_at_given_position(70, 3)
linkedlist.traverse_linkedlist()
linkedlist.delete_at_position(3)
linkedlist.delete_from_beginning()
linkedlist.traverse_linkedlist()
