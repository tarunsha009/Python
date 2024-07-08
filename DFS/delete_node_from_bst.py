# Delete a node from Binary Search Tree
import Node

def find_min(node):
    current  = node
    while current.left is not None:
        current = current.left

    return current


def delete_node(node, key):
    if node is None:
        return node

    if key < node.data:
        node.left = delete_node(node.left, key)
    elif key > node.data:
        node.right = delete_node(node.right, key)
    else:
        if node.left is None:
            temp = node.right
            del node
            return temp
        elif node.right is None:
            temp = node.left
            del node
            return temp

        temp = find_min(node.right)
        node.data = temp.data
        node.right = delete_node(node.right, temp.data)

    return node


def driver():
    root = Node.Node(8)
    root.insert_nodes([3,1,6,7,10,14,4], root)
    Node.in_order_traversal(root)
    print("\nDelete 10")
    result = delete_node(root, 10)
    print("deleted the following", result)
    print("Inorder traversal: ", end=' ')
    Node.in_order_traversal(root)
    print("\n")
    testcase2()
    print("\n")


def testcase2():
    root = Node.Node(2)
    root.insert_nodes([3,4,5,6,7], root)
    Node.in_order_traversal(root)
    print("\nDelete 10")
    result = delete_node(root, 6)
    print("deleted the following", result)
    print("Inorder traversal: ", end=' ')
    Node.in_order_traversal(root)


driver()


