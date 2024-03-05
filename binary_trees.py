# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], result= 0) -> int:
        # using DFS
        # data structure is a stack 
        # while the stack is not empty, I will continue to traverse 
        stack = [ (root, 1) ]

        result=0

        if root is None:
            return result
        
        while stack:
            node, level = stack.pop()
            # give me the node at the end and the level 
            if level > result:
                result = level 
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append( (node.right, level +1))
        
        return result
        # if root.left is None and root.right is None:
        #     return level
        
        # if root.left:
        #     left = self.maxDepth(root.left, level+1)
        #     level = max (left, level)
        # if root.right:
        #     right = self.maxDepth(root.right, level + 1)
        #     level = max (right, level)
        # return level