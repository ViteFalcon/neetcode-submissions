from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class KVNode:
    key: int
    value: int
    next: KVNode | None = None

    def __str__(self) -> str:
        return f"({self.key}:{self.value})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, KVNode):
            return False
        return self.key == other.key and self.value == other.value

    __hash__ = object.__hash__


class KVRangeIteration(NamedTuple):
    index: int
    node: KVNode
    prev_node: KVNode | None

    @property
    def is_head(self) -> bool:
        return self.prev_node is None

    @property
    def is_tail(self) -> bool:
        return self.node.next is None


class KVRange:
    def __init__(self, head: KVNode | None, tail: KVNode | None = None):
        self._visited_nodes: set[KVNode] = set()
        self._prev_node: KVNode | None = None
        self._index: int = 0
        self._node = head
        self._end = tail
        self._has_next = head is not None

    @property
    def node(self) -> KVNode | None:
        return self._node

    @property
    def has_next(self) -> bool:
        # return self._node and self._node is not self._end and self._node.next and self._node.next not in self._visited_nodes
        # return self._node and self._node.next and self._node.next not in self._visited_nodes
        return self._has_next

    def advance(self) -> None:
        if not self._has_next:
            return
        self._visited_nodes.add(self._node)
        self._index += 1
        self._prev_node = self._node
        self._node = self._node.next
        not_visited_end = self._end is None or self._end not in self._visited_nodes
        self._has_next = self._node is not None and not_visited_end

    def __iter__(self) -> KVRange:
        return self

    def __next__(self) -> KVRangeIteration:
        if not self._has_next:
            raise StopIteration

        result = KVRangeIteration(
            index = self._index,
            node = self._node,
            prev_node = self._prev_node,
        )
        self.advance()
        return result


class KVList:
    def __init__(self):
        self._head: KVNode | None = None
        self._tail: KVNode | None = None
        self._size: int = 0

    def iterate(self) -> KVRange:
        return KVRange(head = self._head)

    @property
    def is_empty(self) -> bool:
        return self._size == 0

    @property
    def size(self) -> int:
        return self._size

    def find(self, key: int) -> KVRangeIteration | None:
        for iter in self.iterate():
            if iter.node.key == key:
                return iter
        return None

    def append_node(self, node: KVNode) -> bool:
        result = self.find(node.key)
        if result:
            result.node.value = node.value
            return False

        self._size += 1
        # In case the node come from another list, we need to make sure that the
        # new node's next is None
        node.next = None
        if self._tail:
            self._tail.next = node
        else:
            self._head = node
        self._tail = node
        return True

    def insert(self, key: int, value: int) -> bool:
        return self.append_node(KVNode(key, value))

    def delete(self, key: int) -> KVNode | None:
        result = self.find(key)
        if not result:
            return None

        self._size -= 1
        deleted_node = result.node
        if result.is_head:
            self._head = deleted_node.next
            if not self._head:
                self._tail = None
        elif result.is_tail:
            self._tail = result.prev_node
            if self._tail is None:
                self._head = None
        if result.prev_node:
            result.prev_node.next = deleted_node.next
        # Make sure that the returned node is not referencing another node since it got deleted
        deleted_node.next = None
        return deleted_node


def get_bucket_index(key: int, capacity: int) -> int:
    return key % capacity


class HashTable:
    
    def __init__(self, capacity: int):
        self._max_load_factor = 0.5
        self._size: int = 0
        self._threshold: float = 0.0
        self._capacity: int = capacity
        self._buckets: list[KVList] = []
        self.resize()

    def _calculate_bucket_index(self, key: int) -> int:
        return get_bucket_index(key, self._capacity) 

    def insert(self, key: int, value: int) -> None:
        index = self._calculate_bucket_index(key)
        if self._buckets[index].insert(key, value):
            self._size += 1
        self.resize()

    def get(self, key: int) -> int:
        index = self._calculate_bucket_index(key)
        itr = self._buckets[index].find(key)
        return itr.node.value if itr else -1

    def remove(self, key: int) -> bool:
        index = self._calculate_bucket_index(key)
        if self._buckets[index].delete(key):
            self._size -= 1
            return True
        return False

    def getSize(self) -> int:
        return self._size

    def getCapacity(self) -> int:
        return len(self._buckets)

    def resize(self) -> None:
        capacity = self._capacity
        load_factor = self._size / capacity
        while load_factor >= self._max_load_factor:
            capacity *= 2
            load_factor = self._size / capacity

        if capacity == len(self._buckets):
            return

        buckets = [KVList() for _i in range(capacity)]
        for bucket in self._buckets:
            for itr in bucket.iterate():
                index = get_bucket_index(itr.node.key, capacity)
                buckets[index].append_node(itr.node)
        self._buckets = buckets
        self._capacity = capacity
