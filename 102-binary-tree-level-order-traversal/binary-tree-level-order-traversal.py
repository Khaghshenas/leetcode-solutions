# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        results = []
        
        while q:

            level_size = len(q)
            res = []
            for i in range(level_size):

                root = q.popleft()
                res.append(root.val)

                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            
            results.append(res)
        
        return results