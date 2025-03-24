class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Step 1: Record positions of all candles
        candles = []
        ## candles_idx holds the sequence number of each candle i.e the order in
        ## which it appears from the left
        candles_idx = {}

        for i in range(len(s)):
            if s[i] == "|":
                candles.append(i)
                candles_idx[i] = i

        ans = []

        for start, end in queries:
            # Binary search for the leftmost candle >= start
            l, r = 0, len(candles) - 1
            left_most_candle = -1
            while l <= r:
                mid = (l + r) // 2
                if candles[mid] >= start:
                    #left_most_candle = mid
                    r = mid - 1
                else:
                    l = mid + 1
            left_most_candle = l

            # Binary search for the rightmost candle <= end
            l, r = 0, len(candles) - 1
            right_most_candle = -1
            while l <= r:
                mid = (l + r) // 2
                if candles[mid] <= end:
                    #right_most_candle = mid
                    l = mid + 1
                else:
                    r = mid - 1
            right_most_candle = r

            # If valid candle bounds are found
            if left_most_candle != -1 and right_most_candle != -1 and left_most_candle < right_most_candle:
                total_between = candles[right_most_candle] - candles[left_most_candle] - (right_most_candle - left_most_candle)
                ans.append(total_between)
            else:
                ans.append(0)

        return ans
