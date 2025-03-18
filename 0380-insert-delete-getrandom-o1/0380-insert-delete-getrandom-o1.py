from random import choice

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx = self.dict[val]
            last_element = self.list[-1]

            ## Put last element at position idx
            self.list[idx] = last_element
            self.dict[last_element] = idx

            del self.dict[val]
            self.list.pop() ## pop takes O(1) time
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.list)
            


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()