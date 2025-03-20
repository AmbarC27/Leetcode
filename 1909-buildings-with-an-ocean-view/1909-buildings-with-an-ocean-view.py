class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ## Going from the left to right
        # stack = []
        # for i in range(len(heights)):
        #     while stack and heights[stack[-1]] <= heights[i]:
        #         stack.pop()
        #     stack.append(i)
        # return stack

        ## Going from the right to left
        ans = []
        for i in range(len(heights)-1,-1,-1):
            if not ans:
                ans.append(i)
            if heights[i] > heights[ans[-1]]:
                ans.append(i)
        return ans[::-1]