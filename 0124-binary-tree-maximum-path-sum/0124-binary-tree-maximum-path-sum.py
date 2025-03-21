# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def maxsum(node):
            if not node:
                return 0
            left = maxsum(node.left)
            right = maxsum(node.right)
            across_sum = node.val + left + right
            ## we take max of the two following in the case that
            ## both left and right are negative values, meaning
            ## node.val > node.val + max(left,right)
            ## An individual node also forms a sequence

            ## could have also done 
            ## path_sum = max(node.val, node.val + left, node.val + right)
            path_sum = max(node.val,node.val + max(left,right))
            nonlocal ans
            ans = max(ans,across_sum,path_sum)
            ## need to pass on value without split at the node
            return path_sum
        maxsum(root)
        return ans
            