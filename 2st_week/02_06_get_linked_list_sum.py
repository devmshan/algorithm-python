class Node:
    def __init__(self, value):
        self.data = value
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
            cur_index +=1
        return cur
    
    def add_node(self, index, value):
        new = Node(value)
        if index == 0:
            new.next = self.head
            self.head = new
            return
        
        new.next = self.get_node(index)
        self.get_node(index-1).next = new
        
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        
        self.get_node(index-1).next = self.get_node(index).next
        
    def len(self):
        cur = self.head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next

        return length        
    
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

def get_linked_list_sum(linked_list_1, linked_list_2):

    return get_single_linked_list_sum(linked_list_1) + get_single_linked_list_sum(linked_list_2)

def get_single_linked_list_sum(linked_list):
    cur = linked_list.head
    sum = 0
    for i in range(linked_list.len()):
        sum = sum * 10 + cur.data
        cur = cur.next
    return sum

print(get_linked_list_sum(linked_list_1, linked_list_2))