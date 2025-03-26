class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        for spell in spells:
            min_successful_potion = success/spell
            ## Need to find the index at which we can insert min_successful_potion
            l = 0
            r = len(potions) - 1
            while l <= r:
                mid = (l+r)//2
                if min_successful_potion <= potions[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            idx_of_insertion = l
            pairs.append(len(potions)-idx_of_insertion)
        return pairs