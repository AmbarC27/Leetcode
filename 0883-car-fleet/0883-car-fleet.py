class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars_speed = {position[i]: speed[i] for i in range(n)}
        position_sorted = sorted(position,reverse=True)
        time_to_dest = [0]*n
        for i in range(n):
            time = (target - position_sorted[i])/cars_speed[position_sorted[i]]
            time_to_dest[i] = time
        stack = []
        ans = n
        for i in range(n):
            stack.append(time_to_dest[i])
            ## Remember stack is getting created in a way such that
            ## vehicles closer to the finish line are added first to
            ## the stack, so if any vehicle which is behind in the stack
            ## reaches finish line faster or same time i.e time_to_dest[i]
            ##  is smaller or equal, they would cluster into a fleet, which
            ## could be represented in the stack as popping the top car
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)


        