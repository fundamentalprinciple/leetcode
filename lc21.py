# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not(list1 and list2):
            if list1:
                return list1
            else:
                return list2     
        if list1.val <= list2.val:
            head,a,c=list1,list1,list1.next
            b=list2
        else:
            head,a,c=list2,list2,list2.next
            b=list1
        while(b or c):
            if b and c:
                if b.val <= c.val:
                    a.next,a,b=b,b,b.next
                else:
                    a.next,a,c=c,c,c.next
            else:
                if b:
                    a.next,a,b=b,b,b.next
                    break
                elif c:
                    a.next,a,c.next=c,c,c.next
                    break
        return head 
