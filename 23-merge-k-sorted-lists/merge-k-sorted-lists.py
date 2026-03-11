# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k==0:
            return None
        if k==1:
            return lists[0]
        
        mid = k//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge_two(left, right)
    
    def merge_two(self, l1: [ListNode], l2: [ListNode]) -> ListNode:

        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val<=l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        
        tail.next = l1 if l1 else l2

        return dummy.next






        