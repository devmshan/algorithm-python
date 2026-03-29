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
        
    def len(self):
        length = 0
        cur = self.head
        while cur is not None:
            length += 1
            cur = cur.next
        return length
        
    #끝에서 부터 k번째 노드 값
    def get_kth_node_from_last1(self, k):
        length = self.len()
        # k가 유효 범위를 초과한 경우
        if k < 1 or k > length:
            print(f'유효하지 않은 k값입니다. (k: {k}, 리스트 길이: {length})')
            return None
        cur = self.head
        array = [0]*length
        for i in range(length):
            array[length -1 -i] = cur.data
            cur = cur.next
        return array[k-1]
    
    #끝에서 부터 k번째 노드 값
    def get_kth_node_from_last2(self, k):
        length = self.len()
        # k가 유효 범위를 초과한 경우
        if k < 1 or k > length:
            print(f'유효하지 않은 k값입니다. (k: {k}, 리스트 길이: {length})')
            return None
        cur = self.head
        end_length = length - k
        for i in range(end_length):
            cur = cur.next
        return cur.data
    
    def get_kth_node_from_last3(self, k):
        length = self.len()
        # k가 유효 범위를 초과한 경우
        if k < 1 or k > length:
            print(f'유효하지 않은 k값입니다. (k: {k}, 리스트 길이: {length})')
            return None
        
        slow = self.head
        fast = self.head
        
        for i in range(k):
            fast = fast.next
        print(fast.data)
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        #return slow.data
            

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
# 7나와야 함
print(linked_list.get_kth_node_from_last3(2))