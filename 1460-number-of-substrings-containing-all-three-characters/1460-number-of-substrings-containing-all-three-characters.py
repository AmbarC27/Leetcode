class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        r = 0
        total = 0
        freq = {"a":0,"b":0,"c":0}

        while r < len(s):
            freq[s[r]] += 1

            ## When freq has non-zero amount of each character
            while min(freq.values()) > 0:
                ## All substrings from current window to end are valid
                total += (len(s) - r)

                freq[s[l]] -= 1
                l += 1
            
            r += 1
        
        return total