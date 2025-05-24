# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        minheap = []
        heapq.heapify(minheap)
        index = 0
        for head in lists:
            ## Don't push empty nodes
            if head:
                heapq.heappush(minheap, (head.val,[index,head]))
                ## In internal operation of python heapq, in the heapq.heappush 
                ## function if the first value (in this case head.val) are equal,
                ## the heapq operation looks at the next available values for
                ## comparison, and these values have to be passed in a list. So  
                ## these tiebreaker comparisons are made on the first values of these 
                ## lists. We have arbitrarily given a number which changes (increments
                ## in this case)
                index += 1
        curr = dummy
        while minheap:
            _ , [_,nxt] = heapq.heappop(minheap)
            curr.next = nxt
            curr = curr.next
            if nxt.next:
                heapq.heappush(minheap, (nxt.next.val,[index,nxt.next]))
            # curr = curr.next ## Updating curr works either before or after
            ## pushing to the minheap
            index += 1
        return dummy.next