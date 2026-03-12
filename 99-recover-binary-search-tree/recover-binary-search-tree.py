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
        def inorderTraversal(root):
            if not root:
                return []
            return inorderTraversal(root.left)+[root]+inorderTraversal(root.right)

        sorted_nodes = inorderTraversal(root)
        violations = 0
        first = second = None
        for i in range(len(sorted_nodes)-1):
            if sorted_nodes[i].val>sorted_nodes[i+1].val:
                 
                if not first:
                    first = sorted_nodes[i]
                    second = sorted_nodes[i+1]
                else:
                    second = sorted_nodes[i+1]
                    break

        first.val, second.val = second.val, first.val            


        