class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ## Sweep line algorithm
        kilometre_mark = {}
        for passengers,source,destination in trips:
            kilometre_mark[source] = kilometre_mark.get(source,0) + passengers
            kilometre_mark[destination] = kilometre_mark.get(destination,0) - passengers

        passengers_in_car = 0
        for trip_point in sorted(kilometre_mark.keys()):
            passengers_in_car += kilometre_mark[trip_point]
            if passengers_in_car > capacity:
                return False
        return True