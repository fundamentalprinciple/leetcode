# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Recursive
        if head == None or head.next == None:
            return head
        if head.next.next == None:
            a = head.next
            head.next, a.next = None, head
            return a 
        b = head    
        head = Solution().reverseList(head.next)   
        if b.next.next == None:
            c = b.next
            b.next, c.next = None, b
        return head
        
        '''
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
        '''
