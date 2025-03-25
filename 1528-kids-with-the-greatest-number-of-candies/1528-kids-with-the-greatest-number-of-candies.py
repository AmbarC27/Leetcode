class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # n = len(candies)
        # max_exclude = [0] * n
        # ans = [False] * n
        # for i in range(n):
        #     maxx = 0
        #     for j in range(n):
        #         if i != j:
        #             if candies[j] > maxx:
        #                 maxx = candies[j]
        #     max_exclude[i] = maxx
        # for i in range(n):
        #     if candies[i] + extraCandies >= max_exclude[i]:
        #         ans[i] = True
        # return ans
        ans = []
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans
