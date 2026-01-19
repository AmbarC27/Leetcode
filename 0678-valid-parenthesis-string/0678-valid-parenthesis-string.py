class Solution:
    def checkValidString(self, s: str) -> bool:
        # leftmin = 0 ## tracks min no. open left parentheses
        # leftmax = 0 ## tracks max no. open left parentheses
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         leftmin += 1
        #         leftmax += 1
        #     elif s[i] == ")":
        #         leftmin -= 1
        #         leftmax -= 1
        #     else:
        #         leftmin -= 1
        #         leftmax += 1
            
        #     if leftmax < 0:
        #         ## number of closing right brackets is greater
        #         ## than number of open left brackets and we can't
        #         ## recover from this situation
        #         return False
        #     if leftmin < 0:
        #         ## Reset - it is like going back in time and correcting
        #         ## one of the stars from a closing bracket to an opening
        #         ## opening bracket
        #         leftmin = 0

        # if leftmin == 0:
        #     return True
        # return False

        open_brackets = []
        asterisk = []
        for i, char in enumerate(s):
            if char == "(":
                open_brackets.append(i)
            elif char == "*":
                asterisk.append(i)
            else:
                ## Encountering a closing bracket
                if open_brackets:
                    open_brackets.pop()
                elif asterisk:
                    asterisk.pop()
                else:
                    ## Closing brackets cant be balanced by either opening
                    ## brackets or wildcards, thus string is not valid
                    return False
        while asterisk and open_brackets:
            asterisk_idx = asterisk.pop()
            open_brackets_idx = open_brackets.pop()
            if open_brackets_idx > asterisk_idx:
                ## in this case an open bracket is not closed by either
                ## a wildcard or a closing bracket, thus string is invalid
                return False
        
        if open_brackets:
            ## Not all open brackets are closed and we have exhausted all
            ## the wildcards, thus string is invalid
            return False
        else:
            return True