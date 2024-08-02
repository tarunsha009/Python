class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root):
    if not root:
        return

    # Initialize a stack and push the root node
    stack = [root]
    prev = None

    while stack:
        # Pop a node from the stack
        curr = stack.pop()

        # If there was a previous node, update its right child to the current node
        if prev:
            prev.left = None
            prev.right = curr

        # Push the right and then left child to the stack (pre-order: root, left, right)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

        # Update the previous node to the current node
        prev = curr


# Helper function to print the "linked list" from the tree root
def print_linked_list(root):
    while root:
        print(root.val, end=" -> ")
        root = root.right
    print("None")


# Example usage:
# Constructing the binary tree
#         1
#        / \
#       2   5
#      / \   \
#     3   4   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

# Flatten the tree
flatten(root)

# Print the flattened "linked list"
print_linked_list(root)
ans = []

ans.reverse()