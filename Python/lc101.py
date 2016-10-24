# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
traverse the tree in order  middle->left->right and middle->right->left and record the val of each node, compare whether the val lists
got are same
'''


class Solution(object):
    
    def recursiveLeft(self,root,ll):
        if not root:
            ll.append('')
            return
        ll.append(root.val)
        
        self.recursiveLeft(root.left,ll)
        self.recursiveLeft(root.right,ll)
        
    def recursiveRight(self,root,ll):
        if not root:
            ll.append('')
            return
        ll.append(root.val)
        
        self.recursiveRight(root.right,ll)
        self.recursiveRight(root.left,ll)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.left = []
        self.right = []
        self.recursiveLeft(root,self.left)
        self.recursiveRight(root,self.right)
        
        return self.left==self.right
        
