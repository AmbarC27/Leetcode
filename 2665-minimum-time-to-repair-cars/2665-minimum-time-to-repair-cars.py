class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()

        def can_repair(k):
            num_cars_which_can_be_repaired = 0
            for rank in ranks:
                ## r*n**2 <= k thus n**2 <= (k/r)
                n_squared = k/rank
                n = math.floor(math.sqrt(n_squared))
                num_cars_which_can_be_repaired += n
            return num_cars_which_can_be_repaired >= cars

        l = 0
        r = min(ranks) * cars**2
        ## In Koko eating banana type of problems (monotonic true/false range)
        ## looping condition should be l < r (strictly lesser than)
        while l < r:
            mid = (l+r)//2
            if can_repair(mid):
                r = mid
            else:
                l = mid + 1
        return r