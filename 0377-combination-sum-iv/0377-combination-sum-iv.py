class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        def countways(target):
            if target in cache:
                return cache[target]
            if target == 0:
                return 1
            ans = 0
            for num in nums:
                if num <= target:
                    ans += countways(target - num)
            cache[target] = ans
            return ans
        return countways(target)