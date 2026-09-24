from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: Node | None = None

class LinkedList:
    
    def __init__(self):
        self._head: Node | None = None
        self._tail: Node | None = None
    
    def get(self, index: int) -> int:
        node = self._head
        i = 0
        while node is not None:
            if i == index:
                return node.value
            node = node.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_head = Node(val, self._head)
        if self._head is None:
            self._tail = new_head
        self._head = new_head

    def insertTail(self, val: int) -> None:
        new_tail = Node(val)
        if self._tail is None:
            self._head = new_tail
        else:
            self._tail.next = new_tail
        self._tail = new_tail

    def remove(self, index: int) -> bool:
        node = self._head
        prev_node = None
        i = 0
        while node:
            if i != index:
                i += 1
                prev_node = node
                node = node.next
                continue

            if prev_node:
                prev_node.next = node.next
                if prev_node.next is None:
                    self._tail = prev_node
            else:
                self._head = node.next
                if self._head is None:
                    self._tail = None
            node.next = None
            return True
        return False

    def getValues(self) -> List[int]:
        values = []
        node = self._head
        while node:
            values.append(node.value)
            node = node.next
        return values
