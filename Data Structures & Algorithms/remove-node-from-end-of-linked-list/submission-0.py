# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        dupli=dummy
        actual=dummy
        for i in range(n+1):
            dupli=dupli.next
        while dupli:
            dupli=dupli.next
            actual=actual.next
        actual.next=actual.next.next
        return dummy.next