from binarytree import build
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def print_preorder(root):
    if root:
        print(root.val, end=' ')
        print_preorder(root.left)
        print_preorder(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    tree_list = [1,2,3,4,5]
    visual_tree = build(tree_list)
    print("\nBinary Tree Visualization: ")
    print(visual_tree)

    print("\npreorder traversal of binary tree is: ")
    print_preorder(root)
    print()
