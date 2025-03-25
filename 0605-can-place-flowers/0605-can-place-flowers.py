class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n == 0

        ## Case when length of array >= 2
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            else:
                ## We check the two adjacent plots
                if flowerbed[i-1:i+2] == [0,0,0]:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0