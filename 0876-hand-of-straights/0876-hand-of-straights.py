class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        minheap = []
        for num in count.keys():
            minheap.append(num)
        heapq.heapify(minheap)

        # while minheap:
        for _ in range(len(hand)//groupSize):
            lowest_available_num = minheap[0]
            for num in range(lowest_available_num,lowest_available_num + groupSize):
                if num not in count:
                    return False
                count[num] -= 1
                if count[num] == 0:
                    if num != minheap[0]:
                        ## We should only pop from the minheap if the min Value
                        ## is also the first in the range (lowest_available_num,
                        ## lowest_available_num + groupSize). If we are popping a
                        ## number from the middle of the range, it means we still
                        ## have an occurence of lowest_available_num left in the 
                        ## count dictionary but there would be a hole in the range
                        ## (lowest_available_num, lowest_available_num + groupSize)
                        return False
                    heapq.heappop(minheap)
        return True