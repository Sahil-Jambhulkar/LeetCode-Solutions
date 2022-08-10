# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        def dfs(root):
            
            if not root:
                return []
            
            return [root.val,*dfs(root.left),*dfs(root.right)]
        
        
        lst=dfs(root)
        
        sortedlst=sorted(lst)
        
        return sortedlst[k-1]