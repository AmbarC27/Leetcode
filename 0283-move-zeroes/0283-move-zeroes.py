class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_to_insert_num = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[idx_to_insert_num] = nums[i]
                idx_to_insert_num += 1
            i += 1
        
        ## At this point idx_to_insert_num points to the index where we need
        ## to insert the first zero
        for idx in range(idx_to_insert_num,len(nums)):
            nums[idx] = 0