class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        digit_length = len(str(n))
        ans = []
        def generate(curr_num):
            if len(curr_num) > digit_length:
                return
            if len(curr_num) <= digit_length and int(curr_num) <= n:
                ans.append(int(curr_num))
            for digit in "0123456789":
                generate(curr_num + digit)

        ## Starting backtrakcing of first digit outside the backtracking function
        ## to avoid having a number beginning with a zero
        for digit in "123456789":
            generate(digit)
        return ans
