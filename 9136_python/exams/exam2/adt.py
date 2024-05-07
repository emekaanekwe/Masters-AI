'''STACKS'''
#FIFO structure
#common operations
    #push() - places item at the end of the stack/list
    #pop() - removes item from end of list

class Stack:

    # creates a new stack
    def __init__(self):
        self.the_stack = [] # represent the stack as a list
        self.count = 0 # indicate the current size of the stack
        self.top = -1 # indicate the top position of the stack
        
    # returns the number of items in the stack
    def __len__(self):
        return self.count
        
    # returns True if the stack is empty or False otherwise
    def is_empty(self):
        return len(self) == 0
        
    # pushes an item onto the top of the stack
    def push(self, item):
        self.the_stack.append(item)
        self.top += 1
        self.count += 1
        
    # removes and returns the top item on the stack
    def pop(self):
        assert not self.is_empty(), "Cannot pop from an empty stack"
        
        item = self.the_stack[self.top]
        self.top -= 1
        self.count -= 1
        del self.the_stack[len(self)]
        return item
        
    # returns the item on the stack without removing it
    def peek(self):
        assert not self.is_empty(), "Cannot peek at an empty stack"
        item = self.the_stack[self.top]
        return item

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.the_stack)
stack.push(42)
print(stack.the_stack)
stack.pop()
print(stack.the_stack)

'''QUEUE'''
#Has a LIFO structure
#Best initialize with length in zeroes
#Has bounded capacity
#Common operations
    #append() - adds an item to the beggining of the list/queue
    #serve() - returns the first item
    
    

class Queue:
    '''implementation of the Queue ADT using an array structure with bounded capacity'''

    # creates a new queue
    def __init__(self, size):
        self.the_queue = [0] * size # represent a queue with fixed size
        self.count = 0
        self.front = 0
        self.rear = len(self.the_queue) - 1
        
    # returns the number of items in the queue
    def __len__(self):
        return self.count
        
    # returns True if the queue is empty or False otherwise
    def is_empty(self):
        return len(self) == 0
        
    # returns True if the queue is full or False otherwise
    def is_full(self):
        return len(self) == len(self.the_queue)
        
    # appends the given item to the end of a circular queue
    def append(self, item):
        assert not self.is_full(), "Cannot append to a full queue"
        self.rear = (self.rear + 1) % len(self.the_queue)
        self.the_queue[self.rear] = item
        self.count += 1
        
    # removes and returns the first item of a circular queue
    def serve(self):
        assert not self.is_empty(), "Cannot serve an empty queue"
        item = self.the_queue[self.front]
        self.front = (self.front + 1) % len(self.the_queue)
        self.count -= 1
        
        return item

queue = Queue(5)

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue.the_queue)

print(queue.serve())
print(queue.the_queue)
