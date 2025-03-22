class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome_substr(l,r,s):
            ## l and r are inclusive bounds
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                ## One mismatch found
                return palindrome_substr(l+1,r,s) or palindrome_substr(l,r-1,s)
        return True