class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = TrieNode()
        for num in arr1:
            num = str(num)
            node = root
            for digit in num:
                if digit not in node.children:
                    node.children[digit] = TrieNode()
                node = node.children[digit]

        ans = 0
        for num in arr2:
            num = str(num)
            node = root
            length = 0
            for digit in num:
                if digit in node.children:
                    length += 1
                    node = node.children[digit]
                else:
                    break
            ans = max(ans,length)
        print(root.children)
        return ans