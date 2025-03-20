class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        a = 0
        for a in range(n-3):
            if a > 0 and nums[a-1] == nums[a]:
                continue
            threesum_target = target - nums[a]
            for b in range(a+1,n-2):
                if b > a+1 and nums[b-1] == nums[b]:
                    continue
                c = b + 1
                d = n - 1
                while c < d:
                    threesum = nums[b] + nums[c] + nums[d]
                    if threesum == threesum_target:
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                        c += 1 ## can move any pointer (c or d)
                        while nums[c-1] == nums[c] and c < d:
                            c += 1
                    elif threesum < threesum_target:
                        c += 1
                    elif threesum > threesum_target:
                        d -= 1
        return ans