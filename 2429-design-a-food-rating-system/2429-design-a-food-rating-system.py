class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods_to_rating = {}
        self.cuisines = {} ## cuisine -> heap(rating,food)
        self.food_to_cuisine = {}

        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]

            self.foods_to_rating[food] = rating
            self.food_to_cuisine[food] = cuisine
            if cuisine not in self.cuisines:
                first_entry = []
                first_entry.append([-rating,food])
                heapq.heapify(first_entry)
                self.cuisines[cuisine] = first_entry
            else:
                heapq.heappush(self.cuisines[cuisine],[-rating,food])

    def changeRating(self, food: str, newRating: int) -> None:
        ## self.foods_to_rating always holds the latest rating
        self.foods_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisines[cuisine],[-newRating,food])

    def highestRated(self, cuisine: str) -> str:
        cuisine_food = self.cuisines[cuisine]
        neg_rating, food = cuisine_food[0]
        while self.foods_to_rating[food] != -1 * neg_rating:
            ## stale entry
            heapq.heappop(cuisine_food)
            neg_rating, food = cuisine_food[0]
        return food



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)