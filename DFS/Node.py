from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, "->", end=' ')
        if self.right:
            self.right.print_tree()

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)


    @staticmethod
    def insert_nodes(nums: list, root):
        for num in nums:
            root.insert(num)




def in_order_traversal(root: Node):
    if root is not None:
        in_order_traversal(root.left)
        print(root.data, "->", end=' ')
        in_order_traversal(root.right)

def pre_order_traversal(root: Node):
    if root is not None:
        print(root.data)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root: Node):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data)

def bfs_with_deque(root: Node):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def bfs_with_array_as_queue(root: Node):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def run():
    root = Node(4)
    root.insert_nodes([2, 1, 3, 6, 5, 7], root)
    print("Inorder traversal: ", end=' ')
    in_order_traversal(root)
    # root.print_tree()
    # print('bfs with deque')
    # bfs_with_deque(root)
    # print('bfs with array as queue')
    # bfs_with_array_as_queue(root)
# root = Node('g')
# root.insert('c')
# root.insert('b')
# root.insert('a')
# root.insert('e')
# root.insert('d')
# root.insert('f')
# root.insert('i')
# root.insert('h')
# root.insert('j')
# root.insert('k')
# root.print_tree()
# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# in_order_traversal(root)
# print('-----------------------------')
# pre_order_traversal(root)
# print('-----------------------------')
# post_order_traversal(root)

# run()

