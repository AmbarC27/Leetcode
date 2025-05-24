class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        min_time = {}
        adj_dict = {} ## DAG mapping manager to subordinates
        for employee_num in range(len(manager)):
            adj_dict[manager[employee_num]]  = adj_dict.get(manager[employee_num],[]) + [employee_num]
        
        def dfs(employee,time):
            min_time[employee] = time
            if employee in adj_dict:
                for subordinate in adj_dict[employee]:
                    dfs(subordinate,time + informTime[subordinate])

        dfs(headID,informTime[headID])
        return max(min_time.values())