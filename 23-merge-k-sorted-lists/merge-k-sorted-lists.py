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
        left_merged = self.mergeKLists(lists[:mid])
        right_merged = self.mergeKLists(lists[mid:])

        return self.merge_two_lists(left_merged, right_merged)
        
    def merge_two_lists(self, left: ListNode, right: ListNode) -> ListNode:

        dummy = ListNode(0)
        tail = dummy

        while left or right:

            if left and right:
                if left.val <= right.val:
                    node = ListNode(left.val, None)
                    tail.next = node
                    tail = tail.next
                    left = left.next
                else:
                    node = ListNode(right.val, None)
                    tail.next = node
                    tail = tail.next
                    right = right.next
            elif left:
                while left:
                    tail.next = left
                    tail = tail.next
                    left = left.next
            else:
                while right:
                    tail.next = right
                    tail = tail.next
                    right = right.next
        
        return dummy.next


        