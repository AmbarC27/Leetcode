class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # edges = {src: [] for src, _ in tickets}
        # tickets.sort()
        # for src, dst in tickets:
        #     edges[src].append(dst)
        # ans = ["JFK"]

        # def dfs(airport):
        #     ## Initially have one airport (JFK) and n tickets to fly, so answer
        #     ## should have JFK plus n other elements, each element representing
        #     ## an airport
        #     if len(ans) == len(tickets) + 1:
        #         return True
        #     ## airport has no outgoing edges, and we don't have a list of size
        #     ## (n+1) so we can't proceed here, we have to backtrack
        #     if airport not in edges:
        #         return False 

        #     ## iterate over a copy of adj[src] as we will be modifying the original
        #     ## edges adjacency dict
        #     copy = list(edges[airport])
        #     for i, next_airport in enumerate(copy):
        #         edges[airport].pop(i)
        #         ans.append(next_airport)
        #         if dfs(next_airport):
        #             ## Found a path
        #             return True
        #         else:
        #             ## Didn't find path so backtrack and try again
        #             ## These two lines reverse the decision from before
        #             ## dfs was called on next_airport
        #             edges[airport].insert(i,next_airport)
        #             ans.pop()
        #     return False

        # dfs("JFK")
        # return ans

        ## Neetcode's solution gives TLE
        # adj = {src: [] for src, dst in tickets}
        # tickets.sort()
        # for src, dst in tickets:
        #     adj[src].append(dst)

        # res = ["JFK"]
        # def dfs(src):
        #     if len(res) == len(tickets) + 1:
        #         return True
        #     if src not in adj:
        #         return False

        #     temp = list(adj[src])
        #     for i, v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(v)
        #         if dfs(v): return True
        #         adj[src].insert(i, v)
        #         res.pop()
        #     return False

        # dfs("JFK")
        # return res

        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]