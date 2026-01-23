# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a = head
        while(a and a.val==val):
            a = a.next
        if a == None:
            return a
        if a.next == None:
            if a.val == val:
                return None
            else:
                head = a
                return head    
        head = a
        b = a.next    
        while(b):
            if b.val == val:
                a.next,b = b.next,b.next
            else:
                a,b = a.next,b.next    
        return head        
