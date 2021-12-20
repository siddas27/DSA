from abc import ABC, abstractmethod
from sys import maxsize


class StackNode():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def push(self, x):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def top(self):
        pass


class StackUsingList(Stack):
    def create(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"

        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return "Stack Underflow"

        return self.stack[len(self.stack)-1]

    def push(self, x):
        if len(self.stack) == maxsize:
            return "Stack Overflow"

        self.stack.append(x)

class StackUsingLinkedList(Stack):
    def create(self):
        self.root = None

    def push(self, x):
        new_node = StackNode(x)
        new_node.next = self.root
        self.root = new_node

    def is_empty(self):
        return self.root == None

    def pop(self):
        if self.root == None:
            return "Stack Underflow"
        temp = self.root
        self.root = self.root.next
        return temp.data

    def top(self):
        if self.root == None:
            return "Stack Underflow"
        return self.root.data

