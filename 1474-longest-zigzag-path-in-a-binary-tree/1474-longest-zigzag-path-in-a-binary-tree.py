# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ## Also check editorial for an approach where we begin zigzag within
        ## the DFS
        def zigzag(node,direction_is_left):
            if (node,direction_is_left) in memo:
                return memo[(node,direction_is_left)]
            if not (node.left or node.right):
                memo[(node,direction_is_left)] = 0
                return memo[(node,direction_is_left)]
            if direction_is_left:
                if node.left:
                    memo[(node,direction_is_left)] = 1 + zigzag(node.left,False)
                else:
                    memo[(node,direction_is_left)] = 0
            else:
                ## direction is right
                if node.right:
                    memo[(node,direction_is_left)] = 1 + zigzag(node.right,True)
                else:
                    memo[(node,direction_is_left)] = 0
            return memo[(node,direction_is_left)]
        
        memo = {}
        max_zigzag = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            curr_zigzag_max = max(zigzag(node,True),zigzag(node,False))
            max_zigzag = max(max_zigzag,curr_zigzag_max)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return max_zigzag