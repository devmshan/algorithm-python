
dict = {"fast": "빠른"}

# put(key, value) -> dictionary 에 key 해당하는 곳에 value 저장해두겠다.
# get(key) -> dictionary 에 key 해당하는 vlaue 를 반환해라

class Dict:
    def __init__(self):
        self.items = [None]*8
        
    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value
        
    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]
    
my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
my_dict.put("333", 7)
my_dict.put("77", 6)

print(my_dict.get("333"))

#하지만 colision 발생 시 문제가 생김 같은 index가 나옴
#배열의 길이는 한정되어 있어서