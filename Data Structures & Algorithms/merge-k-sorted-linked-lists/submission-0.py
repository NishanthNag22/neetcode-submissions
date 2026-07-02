# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        nodes=dummy
        while a and b:
            if a.val<=b.val:
                nodes.next=a
                a=a.next
            else:
                nodes.next=b 
                b=b.next
            nodes=nodes.next
        nodes.next=a if a else b
        return dummy.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        if n==0:
            return
        if n==1:
            return lists[0]
        interval=1
        while interval<n:
            for i in range(0,n-interval,interval*2):
                lists[i]=self.mergeTwoLists(lists[i],lists[i+interval])
            interval*=2
        return lists[0]
        