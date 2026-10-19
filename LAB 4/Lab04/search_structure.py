""" TODO
Author: Cristofer Rojas
Implements Stack and Queue classes to manage data using LIFO and FIFO operations for DFS and BFS pathfinding.
"""


class Queue():
    def __init__(self):
        self.items = []

    def add(self, item) -> None:
        """ "Enqueue" the item to the end of the queue """
        self.items.append(item)

    def remove(self):
        """ "Dequeue" the item from the queue and return it """
        return self.items.pop(0)

    def is_empty(self) -> bool:
        """ Returns whether or not the queue is empty """
        return len(self.items) == 0

    


class Stack():
    def __init__(self):
        self.items = []

    def add(self, item) -> None:
        """ Push an item to the top of the stack """
        self.items.insert(0, item)

    def remove(self):
        """ Pop an item from the stack and return it """
        return self.items.pop(0)

    def is_empty(self) -> bool:
        """ Returns whether or not the stack is empty """
        return len(self.items) == 0
