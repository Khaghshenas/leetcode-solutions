# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        previous_node = first = second = None

        def inorderTraversal(node):
            nonlocal first, second, previous_node
            if not node:
                return
            
            inorderTraversal(node.left)
            
            if previous_node and previous_node.val>node.val:
                if first:
                    second = node
                else:
                    first = previous_node
                    second = node
            
            previous_node = node

            inorderTraversal(node.right)
        
        inorderTraversal(root)
        first.val, second.val = second.val, first.val
                





        