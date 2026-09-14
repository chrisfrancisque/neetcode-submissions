# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
dfs -> for each node if node.left.val < node.val and node.right.val > node.val 
if not return false
O(n) - time complexity
O(n) - space complexity because we have to use recursion



"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
        return dfs(root, float('-inf'), float('inf'))
            
        
        