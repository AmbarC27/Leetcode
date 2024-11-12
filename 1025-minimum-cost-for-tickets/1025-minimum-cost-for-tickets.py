class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = [0]*366
        day_pass = [1,7,30]
        for day in days:
            travel_days[day] = 1
        dp = [-1]*366
        def memoize(day):
            if day > 365:
                return 0
            if dp[day] != -1:
                return dp[day]
            if travel_days[day] == 0:
                return memoize(day+1)
            ans = float("inf")
            for i in range(3):
                ans = min(ans,costs[i] + memoize(day + day_pass[i]))
            dp[day] = ans
            return dp[day]
        
        return memoize(0)