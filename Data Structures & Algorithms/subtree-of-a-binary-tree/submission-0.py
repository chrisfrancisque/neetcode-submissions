# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution where we if the one of the children of root == subroot.val
# we start checking all of the children of that child to see if it == subroot
# if not root and not subRoot return false
# if root.val == subroot.val issubtree(root.right, subroot.right), issubTree(root.left, subroot.left)


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: 
            return True
        if not root:
            return False
    

        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False

            if root.val != subRoot.val:
                return False
            
            return (
    isSameTree(root.left, subRoot.left)
    and isSameTree(root.right, subRoot.right)
)
            
        if isSameTree(root, subRoot):
                return True
        

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

        






        
        
        

        


        