# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        n = len(lists)

        while any(lists):
            min_val = float('inf')
            min_idx = -1
            for i in range(n):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_idx = i
            
            tail.next = lists[min_idx]
            tail = tail.next
            
            lists[min_idx] = lists[min_idx].next if lists[min_idx] else None 


        return dummy.next
