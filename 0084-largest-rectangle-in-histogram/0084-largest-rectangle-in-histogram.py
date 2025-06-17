class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxarea = 0
        for i, h in enumerate(heights):
            start = i ## Location where the current bar can start to count area,
            ## which can potentially be pushed leftwards
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxarea = max(maxarea,height*(i - idx))
                start = idx ## Index where current bar starts counting area
                ## has been pushed leftwards. This happens because we know that
                ## the bar at index idx is larger than the bar at index i and so
                ## we start counting area from index idx
            stack.append([start,h])
        
        ## If stack is non-empty then each bar could have extended its width to
        ## index n
        for i,h in stack:
            maxarea = max(maxarea, h*(n-i))
        return maxarea