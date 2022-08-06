# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        
        def inorder(root):
            if not root:
                return ['10000']
            return [*inorder(root.left),root.val,*inorder(root.right)]
        
        
        def preorder(root):
            if not root:
                return ['10000']
            return [root.val,*preorder(root.left),*preorder(root.right)]
        
        
        res1=inorder(p)
        res2=inorder(q)
        res3=preorder(p)
        res4=preorder(q)
        
        print(res1)
        print(res2)
        print(res3)
        print(res4)
        
        return res1==res2 and res3==res4
        
        
        
        
        