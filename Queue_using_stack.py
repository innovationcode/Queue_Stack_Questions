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

#Implement Queue using two Stack instances
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def enqueue(self, data):
        self.s1.push(data)
    
    def dequeue(self):
        while self.s1.length() is not 1:
            self.s2.push(self.s1.pop())
        
        dequeue_data = self.s1.pop()
        while self.s2.length():
            self.s1.push(self.s2.pop())
        
        return dequeue_data
     
    def peek(self):
        while self.s1.length() is not 1:
            self.s2.push(self.s1.pop())
        
        peek_data = self.s1.pop()
        self.s2.push(peek_data)
        while self.s2.length():
            self.s1.push(self.s2.pop())
        
        return peek_data

