"""Implement Queue using Stack"""

# Need Stack class
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        
    def length(self):
        return len(self.stack)
    
    def print_stack(self):
        for data in self.stack:
            print(data, end = " -> ")

#Check Stack Implementation
s1 = Stack()
s1.push(10)
s1.push(20)
print("It's Stack data :  ", end = " ")
s1.print_stack()

