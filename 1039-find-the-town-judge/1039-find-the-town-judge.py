class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_give = {i:0 for i in range(1,n+1)}
        trust_receive = {i:0 for i in range(1,n+1)}
        for link in trust:
            truster, trustee = link
            trust_receive[trustee] += 1
            trust_give[truster] += 1
        for person in trust_receive.keys():
            if trust_receive[person] == n - 1 and trust_give[person] == 0:
                return person
        return -1
        