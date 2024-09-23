class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def dist(coord):
            x,y = coord
            return x**2 + y**2
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        dir_idx = 0
        max_dist = 0
        curr_pos = [0,0]
        obstacle_set = set()
        for obstacle in obstacles:
            obstacle_set.add(tuple(obstacle))
        for command in commands:
            if command == -1:
                dir_idx = (dir_idx + 1) % 4
            elif command == -2:
                dir_idx = (dir_idx - 1) % 4
            else:
                steps = command
                next_cell = [curr_pos[0]+directions[dir_idx][0],
                            curr_pos[1]+directions[dir_idx][1]] 
                while steps > 0 and tuple(next_cell) not in obstacle_set:
                    steps -= 1
                    curr_pos = next_cell
                    max_dist = max(max_dist,dist(curr_pos))
                    next_cell = [curr_pos[0]+directions[dir_idx][0],
                                curr_pos[1]+directions[dir_idx][1]] 
        return max_dist
