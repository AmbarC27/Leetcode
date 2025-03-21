class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff_arr = []
        for num in arr:
            diff_arr.append([abs(num-x),num])
        heapq.heapify(diff_arr)
        print(diff_arr)
        ans = []
        for i in range(k):
            diff, num = heapq.heappop(diff_arr)
            ans.append(num)
        return sorted(ans)