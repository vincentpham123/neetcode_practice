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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balanced means that each node either has no right or left node 
        # or exactly two, also that the height does not exceed 1 difference

        # in order to check that, i need my basecase to check when it is no longer a root
        # so when there is no right or left. what do i bubble up

        def dfs(root):
            if not root:
                return [True, 0]
            # this will allow me to keep track of left and right presence and the height

            left = dfs(root.left)
            right = dfs(root.right)

            # i need to check that left and right are both true and the heightr difference is 1 or 0

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1]) ]
        return dfs(root)[0]