# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        
        
        def valid(left,root,right):
            
            if not root:
                return True
            
            if not(left<root.val and right>root.val):
                return False
            
            return valid(left,root.left,root.val) and valid(root.val,root.right,right)
        
        return valid(-math.inf,root,math.inf)
            
            
            
            
        