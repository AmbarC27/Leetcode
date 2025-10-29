class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ## Holds prereq courses for each course
        prerequisite_set = [set() for _ in range(numCourses)]

        ## We will map the graph direction going from post-requisite to
        ## prerequisites
        adj_dict = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            adj_dict[b].append(a)

        ## returns list of prereqs for course i
        def dfs(i):
            if prerequisite_set[i]:
                return prerequisite_set[i]
            ans = []
            for nei in adj_dict[i]:
                ans.append(nei)
                ans.extend(dfs(nei))
            prerequisite_set[i] = set(ans)
            return prerequisite_set[i]

        for i in range(numCourses):
            dfs(i)

        ans = []
        for u,v in queries:
            ans.append(u in prerequisite_set[v])
        return ans