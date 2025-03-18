class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        triples = []
        for i in range(len(username)):
            triple = [username[i],timestamp[i],website[i]]
            triples.append(triple)
        ## sort by timestamp
        triples = sorted(triples, key = lambda x: x[1])

        ## doubles stores user -> site
        ## site is stored in list in order of visit by the user
        doubles = {}
        for user,time,site in triples:
            if user not in doubles:
                doubles[user] = [site]
            else:
                doubles[user].append(site)

        patterns = {}
        for user in doubles.keys():
            sites = doubles[user]
            n = len(sites)
            if n < 3:
                continue
            # for i in range(n-2):
            #     for j in range(i+1,n-1):
            #         for k in range(j+1,n):
            #             pattern = (sites[i],sites[j],sites[k])
            #             patterns[pattern] = patterns.get(pattern,0) + 1
            seen = set()  # To track unique patterns for this user
            for i in range(n - 2):
                for j in range(i + 1, n - 1):
                    for k in range(j + 1, n):
                        pattern = (sites[i], sites[j], sites[k])
                        if pattern not in seen:
                            seen.add(pattern)
                            if pattern in patterns:
                                patterns[pattern] += 1
                            else:
                                patterns[pattern] = 1
        max_count = -1
        max_pattern = []
        for pattern, val in patterns.items():
            if val > max_count:
                max_count = val
                max_pattern = [pattern]
            elif val == max_count:
                max_pattern.append(pattern)
        print(patterns)
        print(max_pattern)
        max_pattern = sorted(max_pattern)
        print(max_pattern)
        return max_pattern[0]