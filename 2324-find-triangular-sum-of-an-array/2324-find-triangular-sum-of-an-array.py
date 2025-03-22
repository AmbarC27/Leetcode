class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # newnums = []
        # for i in range(n-1):
        #     newnums.append((nums[i] + nums[i+1]) % 10)

        ## O(1) space approach
        for i in range(n-1):
            nums[i] = (nums[i] + nums[i+1]) % 10
        nums.pop()
        return self.triangularSum(nums)