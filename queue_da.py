# Name: Miles Kesser
# OSU Email: kesserm@oregonstate.edu
# Course: CS261 - _data Structures
# Assignment: 3
# Due _date: October 25th
# Description: Queues
from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-rea_dable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    def get_queue(self):
        """
        Returns queue
        CUSTOM METHOD
        """

        return self._da

    # -----------------------------------------------------------------------
    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end of the queue
        """
        self.get_queue().append(value)

    def dequeue(self) -> object:
        """
        Removes and returns the value from at the beginning of the queue
        """
        if self.size() == 0:
            raise QueueException()

        val = self.get_queue().get_at_index(self.size() - self.size())

        self.get_queue().remove_at_index(self.size() - self.size())
        return val
    # ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":
    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))