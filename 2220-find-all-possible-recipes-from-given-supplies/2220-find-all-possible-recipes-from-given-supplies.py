class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj_dict = {}
        # recipes_set = set(recipes)
        # #ingredients_set = set([item for item in ingredient for ingredient in ingredients])
        # ingredients_set = set()
        supply_set = set(supplies)
        # for recipe in ingredients:
        #     for ingredient in recipe:
        #         ingredients_set.add(ingredient)
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                adj_dict[recipe] = adj_dict.get(recipe,[]) + [ingredient]

        def can_build(ingredient,visited):
            if ingredient in supply_set:
                return True
            if ingredient not in adj_dict:
                return False
            if ingredient in visited:
                return False
            visited.add(ingredient)
            for dependent_ingredient in adj_dict[ingredient]:
                if not can_build(dependent_ingredient,visited):
                    return False
            visited.remove(ingredient)
            ## Either no dependent ingredient, or none of the dependent
            ## ingredients cause a cycle
            return True

        ans = []
        for recipe in recipes:
            if can_build(recipe,set()):
                ans.append(recipe)

        return ans