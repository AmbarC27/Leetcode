class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        ## case when we haven't found it, thus need to insert it

        ## insert in the left-most position (could have also chosen
        ## right-most)

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] >= target:
                r = mid - 1
        return l