# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    #recursive
    a = head
    if head.next.next == None:
        t = head.next
        head.next = None
        t.next = head
        return t
    head = reverse(head.next)    
    if a.next.next == None:
        t = a.next
        a.next = None
        t.next = a
    return head

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #lil bit hardcoding, not a good practice
        if head == None or head.next == None:
            return True
        if head.next.next == None:
            if head.val == head.next.val:
                return True
            else:
                return False

        lagger,slow,fast = head,head,head
        count = -1
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            count+=1
        for i in range(count):
            lagger=lagger.next
        lagger.next = reverse(slow)    
        
        a, b = head, lagger.next

        if fast: #odd
            while(b and b.next):
                if a.val == b.val:
                    a = a.next
                    b = b.next
                else:
                    return False
        else:     #even
            while(b):
                if a.val == b.val:
                    a = a.next
                    b = b.next
                else:
                    return False
        return True            

