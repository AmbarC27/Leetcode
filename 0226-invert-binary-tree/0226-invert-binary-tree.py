# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            ## If no node or leaf node
            return root
        temp = root.right
        root.right = root.left
        root.left = temp
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
        