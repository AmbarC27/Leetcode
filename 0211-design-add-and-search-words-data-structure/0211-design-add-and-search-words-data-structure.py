class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endofword = True

    def search(self, word: str) -> bool:
        def recursive_search(word,curr):
            if len(word) == 0:
                return curr.endofword
            char = word[0]
            if char == ".":
                for child in curr.children:
                    node = curr.children[child]
                    if recursive_search(word[1:], node):
                        return True
                return False
            else:
                if char in curr.children:
                    node = curr.children[char]
                    return recursive_search(word[1:], node)
                else:
                    return False

        return recursive_search(word, self.root)
                    


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)