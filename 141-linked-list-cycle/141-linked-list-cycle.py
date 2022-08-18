# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        hire=head
        turtle=head
        
        
        
        while(turtle and hire and hire.next):
            
            hire=hire.next.next
            turtle=turtle.next
            
            while(hire==turtle):
                return True
           
        return False
        
       