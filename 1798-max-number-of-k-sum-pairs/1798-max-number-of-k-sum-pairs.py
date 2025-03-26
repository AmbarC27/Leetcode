class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = Counter(nums)
        ans = 0
        for num in nums:
            complement = k - num
            if num in hashmap and complement in hashmap:
                if num != complement:
                    if hashmap[num] >= 1 and hashmap[complement] >= 1:
                        ans += 1
                        hashmap[num] -= 1
                        hashmap[complement] -= 1
                elif num == complement:
                    if hashmap[num] >= 2:
                        ans += 1
                        hashmap[num] -= 2
        return ans

        ## Both approaches work
        # nums.sort()
        # l = 0
        # r = len(nums) - 1
        # ans = 0
        # while l < r:
        #     if nums[l] + nums[r] == k:
        #         ans += 1
        #         l += 1
        #         r -= 1
        #     elif nums[l] + nums[r] < k:
        #         l += 1
        #     elif nums[l] + nums[r] > k:
        #         r -= 1
        # return ans