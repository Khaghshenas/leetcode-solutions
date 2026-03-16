# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        s, carry = 0, 0

        while l1 or l2 or carry:
            v_1 = l1.val if l1 else 0
            v_2 = l2.val if l2 else 0
            
            s = (v_1 + v_2 + carry)%10
            carry = (v_1 +v_2 + carry)//10

            node = ListNode(s)
            tail.next = node
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return dummy.next



        