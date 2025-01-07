# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr_one = l1
        ptr_two = l2
        carry = 0
        sentinel = ListNode(0)
        curr = sentinel
        while ptr_one or ptr_two or carry:
            val1 = ptr_one.val if ptr_one else 0
            val2 = ptr_two.val if ptr_two else 0
            summ = val1 + val2 + carry
            col_sum = summ % 10
            carry = summ // 10
            curr.next = ListNode(col_sum)
            curr = curr.next
            ptr_one = ptr_one.next if ptr_one else None
            ptr_two = ptr_two.next if ptr_two else None
        return sentinel.next