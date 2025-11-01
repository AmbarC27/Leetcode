class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append([value,timestamp])
        else:
            self.hashmap[key] = [[value,timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        arr = self.hashmap[key]
        l = 0
        r = len(arr) - 1
        ans = ""
        while l <= r:
            mid = l + (r-l)//2
            ## we want to get a number as high as possible thus push to the right
            ## as much as possible
            if arr[mid][1] <= timestamp:
                ans = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)