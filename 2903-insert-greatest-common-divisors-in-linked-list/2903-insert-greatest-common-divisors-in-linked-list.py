# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(a, b):
            while b != 0:
                temp = a
                a = b
                b = temp % b
            return a

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