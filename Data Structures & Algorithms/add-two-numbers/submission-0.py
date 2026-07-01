# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=curr=None
        carry=0

        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            column=val1+val2+carry
            digit=column%10
            carry=column//10

            if not dummy:
                dummy=ListNode(digit)
                curr=dummy
            else:
                curr.next=ListNode(digit)
                curr=curr.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy