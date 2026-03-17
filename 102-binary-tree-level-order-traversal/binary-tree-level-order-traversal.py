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

        level_size = 0
        result = []

        queue = deque([root])
        while queue:
            
            res = []
            level_size = len(queue)
            for i in range(level_size):
                
                q = queue.popleft()
                res.append(q.val)
                
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
             
            result.append(res)
        return result
            



 