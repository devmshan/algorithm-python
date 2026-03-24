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
    
    
    

linked_list = LinkedList(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(9)
linked_list.append(11)
linked_list.append(13)

linked_list.print_all()

print(linked_list.get_node(10).data)