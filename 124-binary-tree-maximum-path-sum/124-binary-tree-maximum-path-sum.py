# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        self.res=-math.inf
        
        def dfs(root):
            
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            
            temp=max(root.val+max(left,right),root.val)
            ans=max(temp,root.val+left+right)
            
            self.res=max(self.res,ans)
            
            return temp
       
    
        dfs(root)
        return self.res
            
            
            
            
        
        
        