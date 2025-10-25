class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(target):
            remaining = target
            splits = 0
            for num in nums:
                if remaining >= num:
                    remaining = remaining - num
                else:
                    splits += 1
                    remaining = target
                    remaining = remaining - num
            splits += 1 ## add a split once traversal is done
            return splits <= k

        ## split size needs to be at least max(nums) otherwise the
        ## largest element can't be split into its own subarray
        l = max(nums)
        r = sum(nums) ## surely we can create a trivial split by 
        ## putting all numbers into one subarray

        ans = float("inf")
        while l <= r:
            mid = (l+r)//2
            if can_split(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans