# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs, where we have a queue and a res list
# populate the queue initially with root
# while q
# populate some curr list with all children of the list
# append curr list to res list
# append curr list to queue:
# return res
# O(n) time complexity 
# O(n) space

# if not list: return None
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            currList = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    currList.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if currList:
                res.append(currList)
        
        return res


        