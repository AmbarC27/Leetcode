class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        total = 0
        ans = 0

        for i in range(len(nums)):
            total += nums[i]
            if (total - k) in hashmap:
                ans += hashmap[total - k]
            hashmap[total] = hashmap.get(total,0) + 1
        return ans