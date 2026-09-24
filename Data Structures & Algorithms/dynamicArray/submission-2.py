class DynamicArray:
    
    def __init__(self, capacity: int):
        self._arr = [None] * capacity
        self._last_index = 0
        self._size = 0
        self._capacity = capacity

    def get(self, i: int) -> int:
        return self._arr[i]

    def set(self, i: int, n: int) -> None:
        self._arr[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self._arr[self._size] = n
        self._size += 1

    def popback(self) -> int:
        self._size -= 1
        return self._arr[self._size]

    def resize(self) -> None:
        self._arr.extend([None] * self._capacity)
        self._capacity = len(self._arr)

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity