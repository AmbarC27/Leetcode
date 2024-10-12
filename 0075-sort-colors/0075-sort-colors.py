class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for i in range(len(nums)):
            count[nums[i]] += 1
        
        counter = 0
        i = 0
        while i < len(nums):
            for _ in range(count[counter]):
                nums[i] = counter
                i += 1
            counter += 1
        return nums