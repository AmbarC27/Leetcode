class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        x_points = {}
        y_points = {}
        for point in points:
            x,y = point
            points_set.add((x,y))
            x_points[x] = x_points.get(x,[]) + [y] ## vertical
            y_points[y] = y_points.get(y,[]) + [x] ## horizontal

        ans = float("inf")
        for x,y in points:
            for y_coord in x_points[x]:
                for x_coord in y_points[y]:
                    if (x_coord != x and y_coord != y) and (x_coord,y_coord) in points_set:
                        ans = min(ans,abs(x-x_coord)*abs(y-y_coord))

        if ans == float("inf"):
            return 0
        return ans