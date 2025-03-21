# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        sentinel = ListNode(-1)
        sentinel.next = head
        prev = sentinel
        curr = head
        idx = 1

        while idx < left:
            curr = curr.next
            prev = prev.next
            idx += 1

        left_minus_one_idx_node = prev
        left_idx_node = curr

        while idx <= right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            idx += 1
        
        left_minus_one_idx_node.next = prev
        left_idx_node.next = curr

        return sentinel.next