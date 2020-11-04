def main():
    my_list = LinkedList()
    my_list.add(10)
    my_list.add(19)
    print(my_list.print())


class LinkedList:
    head = None
    tail = None

    # Constructs an object of this class with an optional head argument.
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    # Returns a string representation of the LinkedList object.
    def print(self):
        temp = self.head
        string = ''

        while temp is not None:
            string.append("{0} ->".format(temp.val))
            temp = temp.next_node

        string.append("None")
        return string

    def add(self, val):
        if self.head is None:
            head = Node(val)
            tail = head
        else:
            self.tail.next_node = Node(val)
            tail = self.tail.next_node


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


main()
