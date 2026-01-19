# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        count = -1
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            count+=1  
        if fast:
            slow = slow.next   
        a = head
        while(slow):
            for i in range(count):
                a = a.next
                count-=1
            if a.val == slow.val:
                slow = slow.next  
            else:
                return False      
            a = head 
        return True 
