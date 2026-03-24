class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        
    #LinkedList의 가장 끝에 있는 노드에 새로운 노드를 연결해줘
    def append (self, value):
        cur = self.head
        
        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)
        
    #LinkedList에서 저장한 head를 
    def print_all(self):
        cur = self.head
        
        while cur is not None:
            print(cur.data)
            cur = cur.next
        

linked_list = LinkedList(3)
linked_list.append(5)
linked_list.append(8)

linked_list.print_all()