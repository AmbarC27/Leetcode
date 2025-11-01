class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_times.sort(key = lambda x: (x[0],x[1]))
        access_by_employee = {}

        for employee,access_time in access_times:
            access_by_employee[employee] = access_by_employee.get(employee,[]) + [access_time]

        ans = []
        for employee in access_by_employee.keys():
            access_time = access_by_employee[employee]
            queue = collections.deque()
            max_accesses_in_60_min = 0
            for time in access_time:
                hh = int(time[:2])
                mm = int(time[2:])
                minute_of_day = hh*60 + mm
                while queue and queue[0] <= minute_of_day - 60:
                    queue.popleft()
                queue.append(minute_of_day)
                max_accesses_in_60_min = max(max_accesses_in_60_min,len(queue))
            if max_accesses_in_60_min >= 3:
                ans.append(employee)
        return ans