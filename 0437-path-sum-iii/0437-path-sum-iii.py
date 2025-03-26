# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def path_sum(node,curr_sum):
            # if not (node.left or node.right):
            #     if curr_sum + node.val == targetSum:
            #         self.ans += 1
            #     return
            node_val = node.val
            if curr_sum + node_val == targetSum:
                self.ans += 1
            if node.left:
                path_sum(node.left, curr_sum + node_val)
            if node.right:
                path_sum(node.right, curr_sum + node_val)

        if not root:
            return 0        

        self.ans = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            path_sum(node, 0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return self.ans