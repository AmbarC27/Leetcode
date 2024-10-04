class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        n = len(skill)
        l = 0
        r = n-1
        teams = []
        chemistry = 0
        prev_team_score = skill[0] + skill[-1]
        while l < r:
            team_score = skill[l] + skill[r]
            if team_score == prev_team_score:
                teams.append([skill[l],skill[r]])
                chemistry += skill[l]*skill[r]
            else:
                teams = []
                break
            l += 1
            r -= 1
        if not teams:
            return -1
        else:
            return chemistry