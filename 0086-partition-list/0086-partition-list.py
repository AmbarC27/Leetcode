# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser_than_x = ListNode(-1)
        greater_than_x = ListNode(-1)
        lesser_than_x_ptr = lesser_than_x
        greater_than_x_ptr = greater_than_x
        curr = head
        while curr:
            if curr.val < x:
                lesser_than_x_ptr.next = curr
                lesser_than_x_ptr = lesser_than_x_ptr.next
            else:
                greater_than_x_ptr.next = curr
                greater_than_x_ptr = greater_than_x_ptr.next
            curr = curr.next

        greater_than_x_ptr.next = None ## Important line to avoid loop
        lesser_than_x_ptr.next = greater_than_x.next
        return lesser_than_x.next