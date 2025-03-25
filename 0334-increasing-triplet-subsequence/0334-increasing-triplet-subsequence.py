class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ## Could have also used Dp to find the longest increasing 
        ##subsequence
        
        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False