class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # ## This question is topological sorting, not necessarily Kahn's algorithm
        # adj_list = {i:[] for i in range(numCourses)}
        # for course,prereq in prerequisites:
        #     adj_list[course].append(prereq)
        # visited = set()
        # curr_path = set()
        # order = []

        # def dfs(course):
        #     if course in curr_path:
        #         ## cycle detected
        #         return False
        #     if course in visited:
        #         ## course has already been visited before and it didn't 
        #         ## cause issues, so it is good
        #         return True
        #     curr_path.add(course)
        #     for prereq in adj_list[course]:
        #         if prereq in visited:
        #             continue ## course caused no issues in terms of cycles so 
        #             ## it is good
        #         if not dfs(prereq):
        #             return False
        #     curr_path.remove(course) ## done dealing with current node in the path
            
        #     visited.add(course)
        #     order.append(course)
        #     return True


        # for i in range(numCourses):
        #     if not dfs(i):
        #         return []
        # return order

        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for dst, src in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish, output = 0, []
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finish != numCourses:
            return []
        return output
