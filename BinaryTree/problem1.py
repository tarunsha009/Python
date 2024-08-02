class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def create_complete_binary_tree(values):
    if not values:
        return None

    nodes = [Node(val=val) for val in values]
    for i in range(len(values)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(values):
            nodes[i].left = nodes[left_index]
        if right_index < len(values):
            nodes[i].right = nodes[right_index]
    return nodes[0]


# Given values to construct the complete binary tree
values = [1, 2, 3, 4, 5, 6, 7]

# Create the tree
root = create_complete_binary_tree(values)


# Function to print the tree level by level to verify correctness
def print_tree_by_levels(root):
    if not root:
        return
    queue = [root]
    while queue:
        level_nodes = []
        next_queue = []
        for node in queue:
            level_nodes.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        print(level_nodes)
        queue = next_queue


# Print the constructed binary tree
print_tree_by_levels(root)
