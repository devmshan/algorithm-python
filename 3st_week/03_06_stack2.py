class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# head
# [4]

# 3 을 추가해줘
# head
# [3] -> [4]

# 맨 위에 있는 값만 알면 됨.
# 1. push 함수에서 맨 위에 값을 넣을 거고
# 2. pop 함수에서 맨 위의 값을 뺄거고
# 3. peek 함수에서 맨 위의 값을 볼거다

# 5 를 추가해줘
# head
# [5] -> [3] -> [4]

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if (self.is_empty()):
            self.head = Node(value)
        else:
            cur = self.head
            self.head = Node(value)
            self.head.next = cur

    # pop 기능 구현
    def pop(self):
        if (self.is_empty()):
            return
        else:
            cur = self.head
            self.head = cur.next
            return cur.data

    def peek(self):
        if (self.is_empty()):
            return
        else:
            print(self.head.data)

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