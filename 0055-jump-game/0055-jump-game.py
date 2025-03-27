class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # target = len(nums) - 1
        # i = len(nums) - 2
        # while i >= 0:
        #     if i + nums[i] >= target:
        #         target = i
        #     i -= 1
        # if target == 0:
        #     return True
        # return False

        ## Either approach works
        ## Edge case
        if len(nums) == 1:
            return True
        furthest_jump = nums[0] 
        i = 1
        while i <= furthest_jump:
            furthest_jump = max(furthest_jump, i + nums[i])
            if furthest_jump >= len(nums) - 1:
                return True
            i += 1
        return False