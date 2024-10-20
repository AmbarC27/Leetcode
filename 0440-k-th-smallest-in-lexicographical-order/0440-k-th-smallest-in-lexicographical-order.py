class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        i = 1

        # To count how many numbers exist between curr and curr+1
        def count_steps(curr):
            steps = 0
            nei = curr + 1
            while curr <= n:
                steps += min(n + 1, nei) - curr
                curr *= 10
                nei *= 10
            return steps

        while i < k:
            step = count_steps(curr)
            # If the steps are less than or equal to k, we skip this prefix's subtree
            if i + step <= k:
                # Move to the next prefix and increase i by the number of steps we skip
                curr += 1
                i += step
            else:
                # Move to the next level of the tree and increment i by 1
                curr *= 10
                k -= 1

        return curr