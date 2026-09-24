from dataclasses import dataclass

@dataclass
class Node:
    value: int
    prev: Node | None = None
    next: Node | None = None

class Deque:
    
    def __init__(self):
        self._head: Node | None = None
        self._tail: Node | None = None

    def isEmpty(self) -> bool:
        return self._head is None

    def append(self, value: int) -> None:
        new_node = Node(
            value=value,
            prev=self._tail,
        )
        if self._tail is None:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(
            value=value,
            next=self._head,
        )
        if self._head is None:
            self._tail = new_node
        else:
            self._head.prev = new_node
        self._head = new_node

    def pop(self) -> int:
        if self._tail is None:
            return -1
        node = self._tail
        self._tail = node.prev
        node.prev = None
        if self._tail is None:
            self._head = None
        else:
            self._tail.next = None
        return node.value

    def popleft(self) -> int:
        if self._head is None:
            return -1
        node = self._head
        self._head = node.next
        node.next = None
        if self._head is None:
            self._tail = None
        else:
            self._head.prev = None
        return node.value
