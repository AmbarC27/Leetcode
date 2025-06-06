class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while not (a == 0 and b == 0 and c == 0):
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1
            if c_bit != a_bit | b_bit:
                if c_bit:
                    ## c_bit is 1, and as there is a mismatch it must mean that
                    ## both a_bit and b_bit are zero, thus only one of the number's
                    ## bit needs to be flipped
                    flips += 1
                else:
                    ## c_bit is 0, and both a_bit and b_bit are 1 and need to flip
                    if a_bit and b_bit:
                        flips += 2
                    ## c_bit is 0, either a_bit or b_bit is 1, so one needs to flip
                    elif a_bit or b_bit:
                        flips += 1
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return flips