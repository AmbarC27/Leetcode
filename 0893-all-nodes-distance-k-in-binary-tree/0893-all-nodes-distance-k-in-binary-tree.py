# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_dict = {}

        queue = collections.deque()
        ## Queue holds tuple (node, node's parent)
        ## Root has no parent so we add a placeholder parent
        queue.append((root,-1))
        while queue:
            node, parent = queue.popleft()
            ## Condition ensures root's non-existent parents aren't added
            if parent != -1:
                ## Create a bidirectional edge on the graph
                if node.val in adj_dict:
                    adj_dict[node.val].append(parent)
                else:
                    adj_dict[node.val] = [parent]
                ## Create a bidirectional edge on the graph
                if parent in adj_dict:
                    adj_dict[parent].append(node.val)
                else:
                    adj_dict[parent] = [node.val]
            if node.left:
                queue.append((node.left,node.val))
            if node.right:
                queue.append((node.right,node.val))

        traversal_queue = collections.deque()
        traversal_queue.append(target.val)
        dist = 0
        visited = set()
        visited.add(target.val)
        while traversal_queue:
            ans = []
            curr_level = traversal_queue
            traversal_queue = collections.deque()
            while curr_level:
                vertex = curr_level.popleft()
                ans.append(vertex)
                if vertex in adj_dict:
                    for nei in adj_dict[vertex]:
                        if nei not in visited:
                            traversal_queue.append(nei)
                            visited.add(nei)
            if dist == k:
                return ans
            dist += 1
        ## At this point diameter of the graph is lesser than k
        return []
