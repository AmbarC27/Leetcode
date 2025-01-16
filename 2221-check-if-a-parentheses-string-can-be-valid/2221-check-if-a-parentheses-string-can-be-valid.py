class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # def valid(parentheses):
        #     if len(parentheses)//2 == 1 or len(parentheses) < 2:
        #         return False
        #     if parentheses == "()":
        #         return True
        #     if parentheses[0] == "(" and parentheses[-1] == ")":
        #         if valid(parentheses[1:-1]):
        #             return True
        #     for i in range(len(parentheses)):
        #         A = parentheses[:i]
        #         B = parentheses[i:]
        #         if valid(A) and valid(B):
        #             return True
        #     return False

        n = len(s)
        if n % 2 == 1:
            return False
        open_brackets = []
        unlocked = []
        for i in range(n):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            else:
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        
        # Match remaining open brackets and the unlocked characters
        ## open_brackets[-1] < unlocked[-1] because if we want to match an open
        ## bracket i.e "(" then its index needs to be lower than the index of
        ## the unlocked bracket
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        return not open_brackets