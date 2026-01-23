# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=None,next=head)
        a,b = dummy,head
        while(b):
            if a.val==b.val:
                a.next,b=b.next,b.next
            else:
                a,b=a.next,b.next    
        return head
