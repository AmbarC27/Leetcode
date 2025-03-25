class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        words = []
        curr_word = ""
        while i < len(s):
            if s[i] == " ":
                if not curr_word:
                    ## There is extra space
                    i += 1
                else:
                    ## A word just ended
                    words.append(curr_word)
                    curr_word = ""
                    i += 1
            else:
                curr_word = curr_word + s[i]
                i += 1
        
        ## Adding the last word if there is no extra space at the end of s
        if curr_word != "":
            words.append(curr_word)

        words.reverse()
        return " ".join(words)