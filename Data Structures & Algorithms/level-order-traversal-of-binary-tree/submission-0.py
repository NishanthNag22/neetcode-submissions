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
        result=[]
        current=deque([root])
        while current:
            level=len(current)
            temp=[]

            for _ in range(level):
                node=current.popleft()
                temp.append(node.val)

                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
            result.append(temp)
        return result