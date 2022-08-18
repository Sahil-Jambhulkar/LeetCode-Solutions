# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        if not head:
            return False
        
        hire=head
        rab=head.next
        
        
        while(hire and rab and rab.next):
            
            if hire==rab:
                return True
           
            hire=hire.next
            rab=rab.next.next
        
        return False
        