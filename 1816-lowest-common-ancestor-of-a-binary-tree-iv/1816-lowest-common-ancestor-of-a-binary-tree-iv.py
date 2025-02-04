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
        while lca:
            found_in_left = False
            found_in_right = False
            if lca.left:
                found_in_left = search_nodes(lca.left,set(nodes))
            if lca.right:
                found_in_right = search_nodes(lca.right,set(nodes))
            if found_in_left:
                lca = lca.left
            elif found_in_right:
                lca = lca.right
            else:
                ## All nodes are not found in any child so current node
                ## is lca
                return lca
        # node_vals = set()
        # node_queue = collections.deque()
        # node_queue.append(root)
        # while node_queue:
        #     node = node_queue.popleft()
        #     node_vals.add(node.val)
        #     if node.left:
        #         node_queue.append(node.left)
        #     if node.right:
        #         node_queue.append(node.right)
        # print(node_vals)

        # queue = collections.deque()
        # queue.append(root)
        # lca = root
        # while queue:
        #     node = queue.popleft()
        #     if search_nodes(node,node_vals):
        #         lca = node
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        # return lca