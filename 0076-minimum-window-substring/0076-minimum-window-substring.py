class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ## Decrease t_dict occurrence when we encounter a character
        ## in string s . When t_dict value goes to 0 remove it from
        ## curr_set. When l pointer encounters a char in t, increment
        ## t_dict value and add to curr_set
        t_dict = Counter(t)
        curr_set = set()
        for char in t:
            curr_set.add(char)
        ans = "#" * 100001
        l = 0
        r = 0
        while r < len(s):
            if s[r] in t_dict:
                t_dict[s[r]] -= 1
                if t_dict[s[r]] == 0:
                    curr_set.remove(s[r])
            while not curr_set:
                
                if s[l] in t_dict:
                    t_dict[s[l]] += 1
                    if t_dict[s[l]] == 1:
                        curr_set.add(s[l])
                curr_str = s[l:r+1]
                if len(curr_str) < len(ans):
                    ans = curr_str
                l += 1
            r += 1
        if len(ans) == 100001:
            return ""
        return ans