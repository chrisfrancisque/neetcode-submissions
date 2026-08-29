# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        path = []

        longest = [0]

        def explore(node):
            if node is None:
                return
            
            path.append(node)

            if node.left is None and node.right is None:
                if len(path) > longest[0]:
                    longest[0] = len(path)
            

            explore(node.left)
            explore(node.right)

            path.pop()

        explore(root)

        return longest[0]
        