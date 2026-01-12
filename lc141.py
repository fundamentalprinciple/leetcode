# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        element = head
        while(True):  
            if element == None:
                return False
            if type(element.val) != str:
                element.val = str(element.val)
            else:
                return True      
            element = element.next
