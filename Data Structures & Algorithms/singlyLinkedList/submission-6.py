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
        print(f"get({index}) -> ",end='')
        while node is not None:
            print(f'[{i}]={node.value}',end=' ')
            if i == index:
                print("[FOUND]")
                return node.value
            node = node.next
            i += 1
        print("[MISSING]")
        return -1

    def insertHead(self, val: int) -> None:
        new_head = Node(val, self._head)
        if self._head is None:
            self._tail = new_head
        self._head = new_head
        print(f"Values after insertHead({val}): {self.getValues()}")

    def insertTail(self, val: int) -> None:
        new_tail = Node(val)
        if self._tail is None:
            self._head = new_tail
        else:
            self._tail.next = new_tail
        self._tail = new_tail
        print(f"Values after insertTail({val}): {self.getValues()}")

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
            print(f"Values after remove({index}): {self.getValues()}")
            return True
        print(f"No values removed for remove({index})")
        return False

    def getValues(self) -> List[int]:
        values = []
        node = self._head
        while node:
            values.append(node.value)
            node = node.next
        return values
