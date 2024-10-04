class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        n = len(skill)
        l = 0
        r = n-1
        chemistry = 0
        prev_team_score = skill[0] + skill[-1] ## setting it initially
        while l < r:
            team_score = skill[l] + skill[r]
            if team_score == prev_team_score:
                ## every team score should equal the score of team before it,
                ## otherwise can do an early exit
                chemistry += skill[l]*skill[r]
            else:
                chemistry = -1
                break
            l += 1
            r -= 1
        return chemistry