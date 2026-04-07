class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        current_index = len(self.items) - 1
        
        while current_index > 1:
            parent_index = current_index // 2
            if self.items[current_index] > self.items[parent_index]:
                self.items[current_index], self.items[parent_index] = self.items[parent_index], self.items[current_index]
                current_index = parent_index
            else:
                break

max_heap = MaxHeap()
max_heap.insert(3)

#       3       level0
# -> [None, 3]


max_heap.insert(4)

# 1. 맨 뒤에다가 원소를 넣는다.
# 2. 부모와 비교해서 자기가 크면 자리를 바꾼다.
# 3. 2의 과정을 부모가 더 크거나 루트 노드에 달했을때 까지 반복한다.

#       3
#      / 
#     4

#       4
#      / 
#     3
# -> [None, 4, 3]

max_heap.insert(2)

#       4
#      / \
#     3   2
# -> [None, 4, 3, 2]

max_heap.insert(9)

#       4
#      / \
#     3   2
#    / 
#   9

#       4
#      / \
#     9   2
#    / 
#   3

#       9
#      / \
#     4   2
#    / 
#   3
# -> [None, 9, 4, 2, 3]


print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!