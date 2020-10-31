def main():
    my_list = LinkedList();
    my_list.add(10)
    my_list.add(19)
    print(my_list.print())


class LinkedList:
    # Constructs an object of this class with an optional head argument.
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = head

    # Returns a string representation of the LinkedList object.
    def print(self):
        temp = self.head
        string = ''

        while temp != None:
            string.append("{0} ->".format(temp.val))
            temp = temp.next_node

        string.append("None")
        return string

    def add(val, tail=None, head=None):
        if head is None:
            head = Node(val)
            tail = head
        else:
            tail.next_node = Node(val)
            tail = tail.next_node


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


main()
