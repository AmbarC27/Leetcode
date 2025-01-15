class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0]*n
        set_A = set()
        set_B = set()
        count = 0
        for i in range(n):
            a = A[i]
            b = B[i]
            set_A.add(a)
            if a in set_B:
                count += 1
            set_B.add(b)
            if b in set_A:
                count += 1
            ans[i] = count
        return ans