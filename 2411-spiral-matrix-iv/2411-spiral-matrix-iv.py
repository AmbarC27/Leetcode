# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        def in_bound(x,y):
            if 0 <= x < n and 0 <= y < m:
                return True
            return False
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        dir_idx = 0
        curr = head
        x,y = 0,0
        visited = set()
        while curr:
            matrix[y][x] = curr.val
            visited.add((x,y))
            dx,dy = directions[dir_idx]
            nx,ny = x+dx,y+dy
            if in_bound(nx,ny) and (nx,ny) not in visited:
                ## Nothing happens
                pass
            else:
                ## Change direction (only once)
                dir_idx = (dir_idx + 1) % 4
                dx,dy = directions[dir_idx]
                nx,ny = x+dx,y+dy
            ## Do not forget to update values of x and y
            x,y = nx,ny
            curr = curr.next
        return matrix