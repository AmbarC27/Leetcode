class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l,r = 0,0
        while r < len(nums) - 1: ## iteration is over when i reaches last element
        ## at position len(nums) - 1
            farthest_jump = 0 ## can also be l
            for i in range(l,r+1):
                farthest_jump = max(farthest_jump,i + nums[i])
            l = r + 1
            r = farthest_jump
            jumps += 1
        return jumps
