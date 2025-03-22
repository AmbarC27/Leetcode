class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        curr_chars = set()
        ans = 0
        # while r < len(s):
        #     if s[r] not in curr_chars:
        #         curr_chars.add(s[r])
        #         ans = max(ans,len(curr_chars)) ## note len(curr_chars) = r-l+1; that could have worked too
        #         r += 1
        #     elif s[r] in curr_chars:
        #         while s[r] in curr_chars:
        #             curr_chars.remove(s[l]) ## getting first char in substring s[l:r+1] removed till we have a substring with all unique characters again
        #             l += 1
        #         curr_chars.add(s[r]) ## add char when you have ensured last occurence of it has been removed
        #         r += 1
        # return ans

        while r < len(s):
            while s[r] in curr_chars:
                curr_chars.remove(s[l])
                l += 1
            curr_chars.add(s[r])
            ans = max(ans,r-l+1)
            r += 1
        return ans