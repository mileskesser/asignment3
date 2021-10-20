# Name: Miles Kesser
# OSU Email: kesserm@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: October 25th
# Description: Linked Lists

class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self._next = None
        self._value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)
        self._tail = SLNode(None)
        self._head._next = self._tail
        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self._head._next != self._tail:
            cur = self._head._next._next
            out = out + str(self._head._next._value)
            while cur != self._tail:
                out = out + ' -> ' + str(cur._value)
                cur = cur._next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self._head
        while cur._next != self._tail:
            cur = cur._next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head._next == self._tail

    # ------------------------------------------------------------------ #
    def add_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list
        """
        new_link = SLNode(value)
        cur = self._head
        new_link._next = cur._next
        cur._next = new_link

    def add_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list
        """
        new_link = SLNode(value)
        # traverse the list
        cur = self._head
        while cur._next != self._tail:
            cur = cur._next
        new_link._next = cur._next
        cur._next = new_link

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the linked list
        """
        if index < 0 or index > self.length():
            raise SLLException()

        # Initialize new node and set head
        new_link = SLNode(value)
        cur = self._head

        # For inserting to empty list or first position
        if self.length() == 0 or index == 0:
            new_link._next = cur._next
            cur._next = new_link

        # For inserting at last position
        elif index == self.length():
            self.add_back(value)

        # All other position insertions
        else:
            count = 0
            while count < index:
                cur = cur._next
                count += 1
            new_link._next = cur._next
            cur._next = new_link

    def remove_front(self) -> None:
        """
        Removes the first node from the list
        """
        if self.length() == 0:
            raise SLLException()

        # Make first element a placeholder then then point around placeholder to remove
        cur = self._head
        temp = cur._next
        cur._next = temp._next
        temp = None

    def remove_back(self) -> None:
        """
        Removes the last node from the list
        """
        if self.length() == 0:
            raise SLLException()

        # Locate last node and disconnect pointer
        cur = self._head
        while cur._next._next != self._tail:
            cur = cur._next
        cur._next = self._tail

    def remove_at_index(self, index: int) -> None:
        """
        Removes a node from the list given its index
        """
        if index < 0 or index >= self.length() or self.length() == 0:
            raise SLLException()

        cur = self._head
        count = 0

        # Use counter to locate index and remove
        while count < index:
            cur = cur._next
            count += 1
        temp = cur._next
        cur._next = temp._next
        temp = None

    def get_front(self) -> object:
        """
        Returns the value from the first node
        """
        if self.length() == 0:
            raise SLLException()

        cur = self._head
        return cur._next._value

    def get_back(self) -> object:
        """
        Returns the value from the last node in the list
        """
        if self.length() == 0:
            raise SLLException()

        # Locate last node to return value
        cur = self._head
        while cur._next._next != self._tail:
            cur = cur._next
        return cur._next._value

    def remove(self, value: object) -> bool:
        """
        Traverses the list from the beginning to the end and removes the first node inthe list that matches the provided “value” object
        """
        cur = self._head

        # Traverse list until value in node is reached, then remove node. Return Bool
        while cur._next != self._tail:
            if cur._next._value == value:
                cur._next = cur._next._next
                return True
            else:
                cur = cur._next

        return False

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided “value” object
        """
        cur = self._head
        count = 0

        # Traverse list and increase counter when each node with vlaue is reached
        while cur._next != self._tail:
            cur = cur._next
            if cur._value == value:
                count += 1
        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new LinkedList object that contains the requested number of nodes from the
        original list starting with the node located at the requested start index
        """
        new_linked_list = LinkedList()

        if start_index < 0 or size < 0 or (
                start_index + size) > self.length() or start_index > self.length()-1:
            raise SLLException()

        if size == 0:
            return LinkedList()

        cur = self._head
        count = 0

        # Use counter to traverse list and locate index
        while count <= start_index:
            count += 1
            cur = cur._next
        while size > 0:
            # Add values to new linked list
            new_linked_list.add_back(cur._value)
            cur = cur._next
            size -= 1
        return new_linked_list


if __name__ == '__main__':

    '''print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)

    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)'''
    #
    #
    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))

    '''print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))
    #
    #
    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)
    #
    #
    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)

    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))

    #
    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())
    #
    #
    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)
    #
    #
    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))

    #
    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")
    #
    #
    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")'''
