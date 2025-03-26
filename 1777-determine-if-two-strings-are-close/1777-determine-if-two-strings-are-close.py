class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ## We need to check if the counter frequencies of each word are the same
        ## (We dont care which particular element has what count, just that
        ## frequencies should match)
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        char_set1 = set(counter1.keys())
        char_set2 = set(counter2.keys())

        if char_set1 == char_set2:
            return sorted(list(counter1.values())) == sorted(list(counter2.values()))
        return False
        # return counter1 == counter2