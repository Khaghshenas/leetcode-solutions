# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        k = len(lists)
        if k == 0:
            return None
        if k == 1: 
            return lists[0]

        arr = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(arr, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while arr:
            val, i, node = heapq.heappop(arr)
            
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(arr, (node.next.val, i, node.next))
        
        return dummy.next
