# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        pointers = [lists[i] for i in range(len(lists))]
        dummy = ListNode(0)
        tail = dummy

        while any(pointers):

            min_val = float('inf')
            min_i = -1

            for i in range(len(pointers)):
                if pointers[i] and pointers[i].val < min_val:
                    min_val = pointers[i].val
                    min_i = i
                
            pointers[min_i] = pointers[min_i].next
            
            node = ListNode(min_val, None)
            tail.next = node
            tail = tail.next

        return dummy.next   
        