class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []

        # Sort the array
        changed.sort()
        freq = Counter(changed)
        original = []

        for num in changed:
            if freq[num] == 0:
                continue

            freq[num] -= 1
            twice = num * 2
            if freq[twice] == 0:
                return []
            freq[twice] -= 1
            original.append(num)

        return original