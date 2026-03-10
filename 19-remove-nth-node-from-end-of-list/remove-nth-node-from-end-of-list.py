# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head

        # store nodes in list
        while curr:
            nodes.append(curr)
            curr = curr.next

        l = len(nodes)
        remove_index = l - n

        if remove_index == 0:
            return head.next

        prev = nodes[remove_index - 1]
        prev.next = nodes[remove_index].next

        return head
        
        