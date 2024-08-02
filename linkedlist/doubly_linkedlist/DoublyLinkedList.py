from linkedlist.doubly_linkedlist.Node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFirst(self, value):
        newNode = Node(value)
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        return newNode

