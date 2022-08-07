# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        
                
        
        #recurssion
        
        #whenever p and q are guranteed that they are present in tree, 2 case arise
        # 1. either p and q present in different sub tree ->  so each will return p and q respectively.so there will be atleast one node who will get p from one side and q from other side and that node will be LCA(onlt one such node)
        
        # 2. p and q are having desendant relationship...q maybe ansector or p...in this case u will only see q and return..not search for p...and vice versa...whatever node you found will be LCA(node will not receive p and q)
        #t(n)
        
        if not root:
            return None
        
        elif root.val==p.val or root.val==q.val:
            print('asdasd')
            return root
        
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        
        if left and right:
            print('asdsa')
            return root
        
        return left or right
        
        
        
        
        
        
        
        
        
        
        
        
        