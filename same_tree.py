# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder_traversal(self, start, traversal):
        if start:
            if start.left:
                traversal += self.inorder_traversal(start.left, traversal)
            else:
                traversal.append()
            traversal.append(start.val)
            if start.right:
                traversal += self.inorder_traversal(start.right, traversal)
            else:
                traversal.append('-')
        return traversal

    def isSameTree(self, p, q):

        traversal_p = []
        traversal_q = []
        if self.inorder_traversal(p, traversal_p) == self.inorder_traversal(q, traversal_q):
            return 'true'
        else:
            return 'false'

