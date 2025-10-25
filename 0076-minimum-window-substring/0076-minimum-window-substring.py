class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        ans, ansLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            ## note that if window[c] surpasses countT[c], that doesn't increase 
            ## have
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < ansLen:
                    ans = [l, r]
                    ansLen = r - l + 1

                window[s[l]] -= 1
                ## note it is not window[s[l]] != countT[s[l]] as window[s[l]] could
                ## also be higher than countT[s[l]]
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        ## Note: don't use l and r as the final answer indices as they may be different
        ## from the actual indices, as the window rolls on. For example, r would always be
        ## len(s)
        starting_idx, ending_idx = ans
        return s[starting_idx : ending_idx + 1] if ansLen != float("infinity") else ""