# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(t1, t2):
            if not t1 and not t2:   # both are None
                return True
            if not t1 or not t2:    # one is None, the other isn’t
                return False
            if t1.val != t2.val:    # values don’t match
                return False
            # check outer & inner pairs
            return symmetric(t1.left, t2.right) and symmetric(t1.right, t2.left)
        
        return symmetric(root.left, root.right)