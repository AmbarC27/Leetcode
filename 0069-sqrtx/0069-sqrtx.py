class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = -1
        while l <= r:
            mid = (l+r)//2
            if mid**2 <= x:
                ## Want to push rightwards as much as possible
                ans = mid
                l = mid + 1
            elif mid ** 2 > x:
                r = mid - 1

        ## Could have also returned r as answer, as we are pushing
        ## as right-most as possible
        return ans