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
        nxt = head.next
        while nxt:
            gcd_val = gcd(curr.val,nxt.val)
            gcd_node = ListNode(val=gcd_val)
            gcd_node.next = nxt
            curr.next = gcd_node
            curr = nxt
            nxt = nxt.next
        return head