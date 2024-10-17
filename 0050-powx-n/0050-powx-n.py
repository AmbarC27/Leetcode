class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x = 1/x
            n *= -1
        def pow(x,n):
            if n == 1:
                return x
            if n % 2 == 0:
                return pow(x**2,n//2)
            if n % 2 == 1:
                return x*pow(x**2,(n-1)//2)
        return pow(x,n)