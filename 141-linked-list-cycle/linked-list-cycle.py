# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        seen = set()

        tail = head
        while tail:
           
            if tail in seen:
                return True
            else:
                seen.add(tail)

            tail = tail.next
        
        return False