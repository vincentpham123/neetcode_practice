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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # for this problem, i need to go down the tree one by one
        # lets start at the root, i then check if it is an ancestor of p and q

        current = root

        while True:
            # keep looping until I find it 
            if current.val < p.val and current.val < q.val:
                # if the current value is less than the two targets, then we movew onto the right side
                # if it is in between 
                current = current.right
            elif current.val > p.val and current.val > q.val:
                current = current.left
            else:
                return current
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # i can use levels with array index 
        if not root:
            return []
        result = []

        queue = deque( [(root, 1)])

        while queue:
            node, level = queue.popleft()
            
            if len(result) < level:
                result.append([])
            
            result[level-1].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return result
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        # with the preorder, i need to know where it sits in the inorder array
        # this is so i know what to set left and right to

        mid = inorder.index(preorder[0])
        
        # now that i have the root, i need to set the left and right

        # now that i know where the left is, i need to split up
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        # i know the next in preorder is left
        # i also know that 9 is the only node on the left 
        return root
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []

        def dfs(root):
            if not root:
                result.append('n')
                return 
            
            result.append(str(root.val))

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(','.join(result))
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        self.i = 0

        def dfs():
            if vals[self.i] == 'n':
                self.i += 1 
                return None 
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
