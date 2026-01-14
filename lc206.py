# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #ITERATIVE, THREE POINTERS
        c = head
        if (head):
            if (head.next):
                b = head.next
            else:
                return head    
        else:
            return head

        while(b):
            b.next, c.next = head, b.next
            head, b = b, c.next       
        return head

