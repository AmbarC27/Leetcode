class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2 ## could also do mid= l + (r - l)//2 to avoid overflow
            ## if (l + r) overflows max value for int32 (however python handles this,
            ## other programming languages dont necessarily do so)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        