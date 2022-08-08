"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        res=[]
        
        if not root:
            return root
        
        q=collections.deque()
        q.append(root)
        
        
        while(q):
            
            level=[]
            for i in range(len(q)):
                
                node=q.popleft()
                level.append(node)
                
                if node.left:
                    q.append(node.left)
                  
                if node.right:
                    q.append(node.right)
               
                   
            lenoflevel=len(level)
            for i in range(len(level)):
                if i+1<len(level):
                    level[i].next=level[i+1]
                   
                
               
        return root
                
                
                
                
            
                
                
            
        
        