class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        damage_sum = sum(damage)
        max_damage = max(damage)
        
        if max_damage >= armor:
            return damage_sum - armor + 1
        else:
            return damage_sum - max_damage + 1