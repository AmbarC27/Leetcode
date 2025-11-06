"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(grid):
            grid_sum = sum(sum(row) for row in grid)
            if grid_sum == 0:
                return Node(val=0, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            elif grid_sum == len(grid) * len(grid):
                return Node(val=1, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)

            n = len(grid)
            mid = n // 2

            top_left = build([grid[i][:mid] for i in range(mid)])
            top_right = build([grid[i][mid:] for i in range(mid)])
            bottom_left = build([grid[i][:mid] for i in range(mid, n)])
            bottom_right = build([grid[i][mid:] for i in range(mid, n)])

            return Node(
                val=0,
                isLeaf=False,
                topLeft=top_left,
                topRight=top_right,
                bottomLeft=bottom_left,
                bottomRight=bottom_right
            )
        return build(grid)