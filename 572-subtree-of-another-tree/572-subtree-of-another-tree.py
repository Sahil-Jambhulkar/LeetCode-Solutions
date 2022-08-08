# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        
        if not root:
            return False
        
    
        def sameTree(p,q):
            
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val==q.val and sameTree(p.left,q.left) and sameTree(p.right,q.right):
                return True
           
        
        
        if sameTree(root,subRoot):
            return True
        
        
        if self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot):
            return True
            
      