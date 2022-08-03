# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        
        if not root:
            return []
        
        leftValues=self.preorderTraversal(root.left)
        rightValues=self.preorderTraversal(root.right)
        
        return [root.val,*leftValues,*rightValues]
        
        
        
        
        