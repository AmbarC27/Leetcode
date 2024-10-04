# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        linked_vals = []
        itr = head
        while itr:
            linked_vals.append(itr.val)
            itr = itr.next
        
        def dfs(node):
            if not node:
                return False
            if node.val == head.val:
                if search(node,0):
                    return True
            return dfs(node.left) or dfs(node.right)

        def search(node,idx):
            if not node:
                return False
            if node.val == linked_vals[idx]:
                if idx == len(linked_vals) - 1:
                    ## reached the last index and every value has matched on the path down
                    return True
                else:
                    return search(node.left,idx + 1) or search(node.right, idx + 1)
            else:
                return False

        return dfs(root)