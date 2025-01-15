class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        for char in freq:
            if freq[char] >= 3:
                ans += (freq[char] - 1)//2
        return len(s) - 2*ans