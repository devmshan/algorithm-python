class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            
        cur.next = Node(value)
        
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
            
    def get_node(self, index):
        cur = self.head
        cur_index = 0
        
        while cur_index != index:
            if cur.next is None:
                print("index:", cur_index+1, "이상의 노드는 없습니다.")
                return cur
            cur = cur.next
            cur_index += 1
            
        return cur
    
    def add_node(self, index, value):
        new = Node(value)
        
        if index == 0:
            new.next = self.head
            self.head = new
            return
        
        pre_node = self.get_node(index-1)
        new.next = pre_node.next
        pre_node.next = new
        
        
linked_list = LinkedList(3)
linked_list.append(5)
linked_list.append(7)
linked_list.add_node(1,5)
linked_list.add_node(1,7)
linked_list.add_node(0,7)
linked_list.print_all()