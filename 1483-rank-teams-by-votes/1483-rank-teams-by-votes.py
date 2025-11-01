class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ans = []
        m = len(votes[0])
        teams = list(votes[0])  # all votes contain same set/order of teams

        # counts[team][i] = number of times team is ranked at position i
        counts = {t: [0] * m for t in teams}
        for v in votes:
            for i, t in enumerate(v):
                counts[t][i] += 1

        # Build a min-heap with keys:
        # ( -count_pos0, -count_pos1, ..., -count_pos(m-1), team_letter )
        # Negative counts => "more is better" becomes "smaller tuple", so it pops first.
        heap = []
        for t in teams:
            key = tuple([-counts[t][i] for i in range(m)] + [t])
            heap.append(key)
        heapq.heapify(heap)

        # Pop in order to build the ranked itinerary
        order = []
        while heap:
            *negvec, team = heapq.heappop(heap)
            order.append(team)

        return "".join(order)