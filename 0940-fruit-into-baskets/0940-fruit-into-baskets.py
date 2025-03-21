class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ## Question is basically asking to find the longest subarray
        ## with only two different elements
        fruit_dict = {}
        l = r = 0
        ans = 0
        while r < len(fruits):
            fruit_dict[fruits[r]] = fruit_dict.get(fruits[r],0) + 1
            while len(fruit_dict) > 2:
                fruit_dict[fruits[l]] -= 1
                if fruit_dict[fruits[l]] == 0:
                    del fruit_dict[fruits[l]]
                l += 1
            ans = max(ans,r-l+1)
            r += 1
        return ans