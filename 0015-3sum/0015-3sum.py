class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                ## skipping elements which appear consecutively
                continue
            l = i+1
            r = n-1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1 ## Need to update one of the pointers (could also be r)
                    while nums[l-1] == nums[l] and l < r:
                        ## avoiding situation of consecutive elements again
                        l += 1
        return ans