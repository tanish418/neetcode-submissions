class MyHashMap:

    def __init__(self):
        self.data = {}
        

    def put(self, key: int, value: int) -> None:
        self.data.update({key:value})

    def get(self, key: int) -> int:
        return self.data.get(key,-1)

    def remove(self, key: int) -> None:
        self.data.pop(key,-1)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)