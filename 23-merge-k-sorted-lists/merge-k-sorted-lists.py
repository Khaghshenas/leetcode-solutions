# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two(list1: [ListNode], list2: [ListNode]):
            if not list1:
                return list2
            if not list2:
                return list1

            dummy = ListNode(0)
            tail = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                
                tail= tail.next
            
            tail.next = list1 if list1 else list2
            return dummy.next

        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]

        mid = k//2
        
        return merge_two(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))


        
