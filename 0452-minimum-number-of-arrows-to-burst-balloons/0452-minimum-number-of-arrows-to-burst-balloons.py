class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        ans = 0
        leftmost_balloon_right_border = points[0][1]
        for i in range(1,len(points)):
            start , end = points[i]
            if start <= leftmost_balloon_right_border:
                pass
            else:
                ans += 1
                leftmost_balloon_right_border = end
        ans += 1
        return ans