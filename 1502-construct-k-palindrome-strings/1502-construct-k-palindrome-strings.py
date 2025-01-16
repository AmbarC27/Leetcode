class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        freq = Counter(s)
        one_groups = 0
        two_groups = 0
        for value in freq.values():
            two_groups += value // 2
            one_groups += value % 2
        if one_groups > k:
            return False
        return True