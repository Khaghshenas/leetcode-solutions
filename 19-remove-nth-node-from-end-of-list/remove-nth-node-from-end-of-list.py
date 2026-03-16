# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        #dummy = ListNode(0)
        #tail = dummy

        #fast = dummy
        #slow = dummy

        nodes = []
        node = head
        
        while node:
            nodes.append(node)
            node = node.next
        if len(nodes)==n:
            return head.next
        
        nodes[len(nodes)-n-1].next = nodes[len(nodes)-n].next 

        return head
            

        