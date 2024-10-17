class DetectSquares:

    def __init__(self):
        ## in defaultdict(int) if a key doesn't exist in the dictionary
        ## then 0 is returned as the default value
        # self.points = defaultdict(int)
        self.points = {}
        ## In self.count we iterate over self.points_list instead of self.points 
        ## as iterating over dict keys can give undefined behaviour sometimes
        self.points_list = []

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.points:
            self.points[tuple(point)] += 1
        else:
            self.points[tuple(point)] = 1
        self.points_list.append(point)

    def count(self, point: List[int]) -> int:
        ## strategy is to see if we find a point which is diagonal to our query
        ## point. If we find a diagonal point, we gotta see if we can get points 
        ## in the other diagonal. Note that this approach works for both squares 
        ## and rectangles
        px,py = point
        ans = 0
        for x,y in self.points_list:
            ## First condition ensures diagonality and second condition
            ## ensures we are not considering squares of area 0
            if (abs(x-px) == abs(y-py)) and (x != px and y != py):
                ans += self.points.get((x,py),0) * self.points.get((px,y),0)
        return ans

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)