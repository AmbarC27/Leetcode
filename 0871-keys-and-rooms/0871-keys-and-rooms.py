class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n
        stack = [0]
        # for keys in rooms[0]:
        #     stack.append(keys)
        visited[0] = 1
        while stack:
            nxt = stack.pop()
            for key in rooms[nxt]:
                if visited[key] == 0:
                    visited[key] = 1
                    stack.append(key)
        # if 0 in visited:
        #     print(visited)
        #     return False
        # return True
        return sum(visited) == len(rooms)
        