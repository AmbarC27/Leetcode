class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        ans = 0
        while l <= r:
            both_weight = people[l] + people[r]
            if both_weight > limit:
                ## add the heavier person
                r -= 1
                ans += 1
            else:
                l += 1
                r -= 1
                ans += 1
        return ans