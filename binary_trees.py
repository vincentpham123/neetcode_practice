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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTreeBFS(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True 
        if not p or not q:
            return False 

        queue = deque( [ ( p , q )])

        # have a queue with tuples 

        while queue:
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue
            # if two Nones were added, continue with the loop, to eliminat ethe loop

            if not node1 or not node2 or node1.val != node2.val:
                return False
                # if any of the nodes do not exist or their values are not equal, that means the trees are not the same

            # if they are equal, add to the queue

            queue.append(( node1.left, node2.left ))
            queue.append(( node1.right, node2.right ))
        return True
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, node1, node2):

        if not node1 and not node2:
            return True 
        if node1 and node2 and node1.val == node2.val:
            return self.isSameTree(node1.left,node2.left) and self.isSameTree(node1.right, node2.right)
            # if the values are the same, i need to DFS and check if every value is the same 
        return False