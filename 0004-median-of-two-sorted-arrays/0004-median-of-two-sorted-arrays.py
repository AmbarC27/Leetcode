class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## Ensure A is the shorter array
        if len(nums1) < len(nums2):
            A,B = nums1,nums2
        else:
            B,A = nums1,nums2
        half = (len(nums1) + len(nums2))//2
        l, r = 0, len(A) - 1

        while True:
            ## i is the midpoint pointer for A
            i = (l + r) // 2  # pointer for A
            j = half - i - 2  # pointer for B, subtract 2 as we are dealing with
            ## two arrays

            ## Adding the infinity part to avoid edge cases where we are
            ## going out of bound of the array
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                ## Too many elements in left partition of array A, so make 
                ## it smaller by moving r pointer leftwards
                r = i - 1
            else:
                ## Case when Bleft > Aright i.e second condition in the IF
                ## statement is the one which is not satisfied
                ## Too few elements in left partition of array A, so make 
                ## it larger by moving l pointer rightwards
                l = i + 1