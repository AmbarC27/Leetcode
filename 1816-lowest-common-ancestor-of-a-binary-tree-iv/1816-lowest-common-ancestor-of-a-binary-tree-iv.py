# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def search_nodes(root,nodes_to_search):
            queue = collections.deque()
            queue.append(root)
            nodes_found = 0
            while queue:
                node = queue.popleft()
                if node in nodes_to_search:
                    nodes_found += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return nodes_found == len(nodes_to_search)

        lca = root
        while True:
            # if lca.left:
            #     all_nodes_found_in_left = search_nodes(lca.left,set(nodes))
            # else:
            #     all_nodes_found_in_left = False
            # if lca.right:
            #     all_nodes_found_in_right = search_nodes(lca.right,set(nodes))
            # else:
            #     all_nodes_found_in_right = False
            # if all_nodes_found_in_left:
            #     lca = lca.left
            # elif all_nodes_found_in_right:
            #     lca = lca.right

            ## Simpler logic
            if lca.left and search_nodes(lca.left,set(nodes)):
                lca = lca.left
            elif lca.right and search_nodes(lca.right,set(nodes)):
                lca = lca.right
            else:
                ## All nodes are not found in any child so current node
                ## is lca
                return lca

        ## The method below gives TLE

        # self.lca = root
        # def recurse(curr):
        #     if not curr:
        #         return
        #     if search_nodes(curr,set(nodes)):
        #         self.lca = curr
        #     recurse(curr.left)
        #     recurse(curr.right)

        # recurse(root)
        # return self.lca