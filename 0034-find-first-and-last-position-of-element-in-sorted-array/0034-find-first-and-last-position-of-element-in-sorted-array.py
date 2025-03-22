class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        def num_exists(nums,target):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        if not num_exists(nums,target):
            return [-1,-1]

        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        ## When finding lower bound, lower bound = l
        lower_bound = l
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r+1)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        ## When finding upper bound, upper bound = r
        upper_bound = r
        
        return [lower_bound,upper_bound]