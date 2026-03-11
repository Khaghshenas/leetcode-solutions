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

        return self.two_merge(left, right) 
    
    def two_merge(self, left: ListNode, right: ListNode) -> ListNode:
        if not left:
            return right
        if not right:
            return left
        
        dummy = ListNode(0)
        tail = dummy

        while left or right:
            if left and right and left.val<=right.val:
                node = ListNode(left.val)
                tail.next = node
                tail = tail.next
                left = left.next
            elif left and right and left.val>right.val:
                node = ListNode(right.val)
                tail.next = node
                tail = tail.next
                right = right.next
            elif left:
                while left:
                    node = ListNode(left.val)
                    tail.next = node
                    tail = tail.next
                    left = left.next
            else:
                while right:
                    node = ListNode(right.val)
                    tail.next = node
                    tail = tail.next
                    right = right.next
        
        return dummy.next






        