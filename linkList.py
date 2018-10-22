class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        def __repr__(self):
            return repr(self.data)

class LinkList:
    def __init__(self):
        self.head = Node()              # defining empty node

    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

            # we will print all node as a string and between two node we devided them by comma
            return ",".join(nodes)

    # adding value at end of the list
    def append(self):
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
            return

        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    # adding value at first
    def prepend(self):
        node = None(data, self.head.next)
        self.head.next = node

    def insert(self, data, new_data):
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                new_node = Node(new_data, current_node.next)
                current_node.next = new_node
                break

            current_node = current_node.next


    # searching a node from the list
    def search(self, item):
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node

            current_node = current_node.next
        return None

    def remove(self, item):
        previous_node   = self.head
        current_node    = self.head.next

        while current_node:
            if current_node.data == item:
                break
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return None

        if self.head == previous_node:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next
