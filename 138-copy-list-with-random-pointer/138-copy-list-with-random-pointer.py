"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        m={None:None}
        
        curr=head
        while(curr):
            m[curr]=Node(curr.val)
            curr=curr.next
           
        
        ans=head
        
        while(ans):
            m[ans].next=m[ans.next]
            m[ans].random=m[ans.random]
            ans=ans.next
           
        
        return m[head]
            
           
        
        