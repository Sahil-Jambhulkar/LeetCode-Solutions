# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        
        first=head
    
        while(n):
            first=first.next
            n-=1
           
        
        ptr=dummy=ListNode(0)
        
        dummy.next=head
        print(dummy.next.val)
        print(ptr.next.val)
        
        
        while(first):
            print('asdsad')
            first=first.next
            dummy=dummy.next
           
        dummy.next=dummy.next.next
        
        return ptr.next
            
            
        
        
    