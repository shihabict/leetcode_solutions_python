class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_traversal_type(self, trav_type):
        if trav_type == 'preorder':
            print(self.preorder_traversal(tree.root, []))
        elif trav_type == 'inorder':
            print(self.inorder_traversal(tree.root, []))
        elif trav_type == 'postorder':
            print(self.postorder_traversal(tree.root, []))
        else:
            print("Order type " + str(trav_type) + " is invalid")

    def preorder_traversal(self, start, traversal):
        if start:
            # traversal+=str(start.value)+','
            traversal.append(start.value)
            self.preorder_traversal(start.left, traversal)
            self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        if start:
            self.inorder_traversal(start.left, traversal)
            traversal.append(start.value)
            self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        if start:
            self.inorder_traversal(start.left, traversal)
            self.inorder_traversal(start.right, traversal)
            traversal.append(start.value)
        return traversal


def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    traversal = []

    if root.left:
        self.inorderTraversal(root.left)
    if root:
        traversal.append(root.val)
    if root.right:
        self.inorderTraversal(root.right)


# return map(str,traversal)
return traversal
if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node()
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    # tree.print_traversal_type('preorder')
    # tree.print_traversal_type('inorder')
    tree.print_traversal_type('postorder')
# print(tree)
