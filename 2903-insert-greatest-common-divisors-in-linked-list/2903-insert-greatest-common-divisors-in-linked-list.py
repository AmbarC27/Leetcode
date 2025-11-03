# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        curr = head
        # nxt = head.next
        while curr and curr.next:
            nxt = curr.next
            gcd_val = gcd(curr.val,curr.next.val)
            gcd_node = ListNode(val=gcd_val)
            gcd_node.next = nxt
            curr.next = gcd_node
            curr = curr.next.next
            # nxt = nxt.next
        return head