class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_by_idx = {}
        # candy_by_idx[-1] = -1 ## For easy edge case handling
        # candy_by_idx[len(ratings)] = -1 ## For easy edge case handling

        minheap = [(rating,i) for i,rating in enumerate(ratings)]
        heapq.heapify(minheap)
        candies_per_kid = 1
        total_candies = 0
        while minheap:
            _, idx = heapq.heappop(minheap)
            if idx > 0 and ratings[idx-1] < ratings[idx]:
                candies_relative_to_kid_on_left = candy_by_idx.get(idx-1,0) + 1
            else:
                candies_relative_to_kid_on_left = candies_per_kid
            if idx < len(ratings) - 1 and ratings[idx] > ratings[idx+1]:
                candies_relative_to_kid_on_right = candy_by_idx.get(idx+1,0) + 1
            else:
                candies_relative_to_kid_on_right = candies_per_kid
            candies_for_this_kid = max(
                candies_per_kid,
                max(candies_relative_to_kid_on_left,
                candies_relative_to_kid_on_right)
                )
            print(candies_for_this_kid)
            candy_by_idx[idx] = candies_for_this_kid
            total_candies += candies_for_this_kid
            candies_per_kid = 1
        return total_candies