# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        left = self.flatten(root.left)
        right = self.flatten(root.right)

        if left and right:
            root.right = None
            root.left = None
            root.right = left
            cur_root = root.right
            while cur_root.right:
                cur_root = cur_root.right
            cur_root.right = right
        elif left:
            root.right = None
            root.left = None
            root.right = left
        
        return root
        
        