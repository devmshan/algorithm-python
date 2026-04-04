
dict = {"fast", "빠른"}

class LinkedTuple:
    def __init__(self):
        self.items = []
        
    def add(self, key, value):
        self.items.append((key, value))
        
    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())
        
    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)
        
    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)
    
my_dict = LinkedDict()
my_dict.put("test", 3)
#아래 두개의 hash index 값이 1
#colision 발생
my_dict.put("333", 7)
my_dict.put("77", 6)

#self.items[1] = [7] -> [6]
#그럼 만약
print(my_dict.get("77"))
print(my_dict.get("333"))
#333의 vlaue가 7인지 6인지 알 방법이 없다
#key 값과 value를 같이 저장하도록 자료구조를 변경해야 함
#self.items[1] = ["333",7] -> ["77",6]

# 1. index = hash(333) % len(self.items) -> 1
# 2. self.items[1] 값을 뒤져라
# 3. 이 값은 현재 ["333",7] -> ["77",6] 링크드 리스트
# 4. 그럼 이 링크드 리스트를 순회하면서 key 값이 있는 노드의 value를 가져온다