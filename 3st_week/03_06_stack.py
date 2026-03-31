class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if (self.is_empty()):
            self.head = Node(value)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(value)

    # pop 기능 구현
    def pop(self): 
        if (self.is_empty()):
            print("empty")
            return
        
        cur = self.head
        cur_next = cur.next
        
        if cur_next is None:
            result = cur.data
            self.head = None
        else:
            while cur_next.next is not None:
                cur = cur.next
                cur_next = cur_next.next
            
            result = cur_next.data
            cur.next = None
        
        return result

    def peek(self):
        if (self.is_empty()):
            return
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            print(cur.data)

    # isEmpty 기능 구현
    def is_empty(self):
        if self.head is None:
            return True
        return False
    
first_stack = Stack()
first_stack.push(5)
first_stack.push(4)
first_stack.peek()
first_stack.push(3)
first_stack.push(2)
first_stack.push(1)
print(f"first_stack POP() = {first_stack.pop()}")
first_stack.peek()
print(f"first_stack POP() = {first_stack.pop()}")
print(f"first_stack POP() = {first_stack.pop()}")
print(f"first_stack POP() = {first_stack.pop()}")
print(f"first_stack POP() = {first_stack.pop()}")
print(f"first_stack POP() = {first_stack.pop()}")
first_stack.peek()