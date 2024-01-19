class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
    
    def peek(self):
        if not stack1.is_empty():
            return self.stack[-1]

    def print_stack(self, message):
        print(f"{message} : {self.stack}")

stack1 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)

stack1.print_stack("Items in the stack")

print(f"Peek of the stack: {stack1.peek()}")

stack1.pop()
result= stack1.pop()
print(result)
stack1.print_stack("After removing the last two items")

# Time comlexity is 0(1)
