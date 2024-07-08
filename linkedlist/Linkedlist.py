from linkedlist.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert_at_tail(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = Node(data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def delete_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next

    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def is_empty(self):
        return self.head is None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self.head

    def reverse_list(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return rest