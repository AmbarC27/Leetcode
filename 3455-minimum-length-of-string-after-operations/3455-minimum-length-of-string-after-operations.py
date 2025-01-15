class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        pairs_removed = 0
        for char in freq:
            if freq[char] >= 3:
                pairs_removed += (freq[char] - 1)//2
        return len(s) - 2*pairs_removed