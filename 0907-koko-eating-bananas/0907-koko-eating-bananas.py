class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def speed_verified(k):
            remaining_rounds = h
            for pile in piles:
                if remaining_rounds > 0:
                    remaining_rounds -= (math.ceil(pile / k))
                else:
                    return False ## early exit
            if remaining_rounds >= 0:
                return True
            else:
                return False

        l = 1
        r = max(piles)
        min_k = float("inf")
        ## Return min_k instead of l or r 
        while l <= r:
            mid = l + (r-l)//2
            if speed_verified(mid):
                min_k = mid
                ## min_k = min(min_k,mid) 
                ## Either option of updating min_k works
                r = mid - 1
            else:
                l = mid + 1
        return min_k