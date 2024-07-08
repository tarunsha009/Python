from linkedlist.Linkedlist import LinkedList

linkedlist = LinkedList()
linkedlist.insert_at_tail(1)
linkedlist.insert_at_tail(2)
linkedlist.insert_at_tail(3)
linkedlist.insert_at_tail(4)

linkedlist.print_list()

linkedlist.insert_at_beginning(0)
linkedlist.print_list()
print(linkedlist.search(3))
linkedlist.delete(3)
linkedlist.print_list()
