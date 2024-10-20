class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        digit_length = len(str(n))
        ans = []
        # starting_num = "1" + "0"*(digit_length - 1)
        # for digit in "123456789":
        def generate(curr_num):
            if len(curr_num) > digit_length:
                return
            if len(curr_num) <= digit_length and int(curr_num) <= n:
                ans.append(int(curr_num))
            for digit in "0123456789":
                generate(curr_num + digit)
        for digit in "123456789":
            generate(digit)
        return ans

        # while len(ans) < n:
        #     for digit in "0123456789":

        #     for length in range(1,n+1):
