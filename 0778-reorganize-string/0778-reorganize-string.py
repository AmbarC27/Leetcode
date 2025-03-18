class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_dict = Counter(s)
        minheap = []
        for char,freq in freq_dict.items():
            minheap.append((-1*freq,char))
        heapq.heapify(minheap)
        ans = []
        while len(minheap) > 1:
            neg_x_val, x = heapq.heappop(minheap)
            neg_y_val, y = heapq.heappop(minheap)
            ans.extend([x,y])
            if neg_x_val + 1 != 0:
                heapq.heappush(minheap,(neg_x_val+1,x))
            if neg_y_val + 1 != 0:
                heapq.heappush(minheap,(neg_y_val+1,y))
        if not minheap:
            return "".join(ans)

        ## Case when minheap has one char left
        neg_x_val, x = heapq.heappop(minheap)
        if neg_x_val < -1:
            return ""
        else:
            ## Case when the character left has only one occurence left
            ans.append(x)
            return "".join(ans)
