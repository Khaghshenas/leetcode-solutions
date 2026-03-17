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
        first = second = None
        previous_node = None

        def inorder_traversal(node):
            nonlocal first, second, previous_node

            if not node:
                return

            inorder_traversal(node.left)

            if previous_node and node.val < previous_node.val:
                if not first:
                    first = previous_node
                    
                second = node

            previous_node = node
            inorder_traversal(node.right)
        

        inorder_traversal(root)
        first.val, second.val = second.val, first.val



