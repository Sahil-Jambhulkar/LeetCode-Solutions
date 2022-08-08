# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def mirror(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if p.val==q.val and mirror(p.left,q.right) and mirror(p.right,q.left):
                return True
        
        
        return mirror(root,root)
        