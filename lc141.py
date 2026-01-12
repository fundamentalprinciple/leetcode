# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #Floyd's fast and slow pointers 
        
        slow, fast = head, head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False        


        '''
        MORE EXPLICIT CONDITIONAL EVALUATIONS, BAD FOR READABILITY

        if head == None:
            return False
        else:
            a = head    

        if head.next == None or head.next.next == None:
            return False
        else:
            b = head.next.next  

        while(True):
            if a == b:
                return True

            if a == None:
                return False
            else:
                a = a.next    

            if b.next == None or b.next.next == None:
                return False
            else:
                b = b.next.next    
        '''        



        '''
        BY MUTATING

        element = head
        while(True):  
            if element == None:
                return False
            if type(element.val) != str:
                element.val = str(element.val)
            else:
                return True      
            element = element.next
        '''    
