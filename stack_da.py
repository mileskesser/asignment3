# Name: Miles Kesser
# OSU Email: kesserm@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: October 25th
# Description: Stacks

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da_val = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da_val.length()) + " elements. ["
        out += ', '.join([str(self._da_val[i]) for i in
                          range(self._da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da_val.length()

    def get_list(self):
        """
        Returns input list
        CUSTOM METHOD
        """
        return self._da_val

    # -----------------------------------------------------------------------
    def push(self, value: object) -> None:
        """
        Adds a new element to the top of the stack
        """
        self.get_list().append(value)

    def pop(self) -> object:
        """
        Removes the top element from the stack and returns its value
        """
        if self.size() == 0:
            raise StackException()

        val = self.get_list().get_at_index(self.size() - 1)

        self.get_list().remove_at_index(self.size() - 1)
        return val

    def top(self) -> object:
        """
        Returns the value of the top element of the stack without removing it
        """
        if self.size() == 0:
            raise StackException()

        val = self.get_list().get_at_index(self.size() - 1)
        return val


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
