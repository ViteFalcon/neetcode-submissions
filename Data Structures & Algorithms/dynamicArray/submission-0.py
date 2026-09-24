class DynamicArray:
    
    def __init__(self, capacity: int):
        self._arr = [None] * capacity
        self._last_index = 0
        self._size = 0
        self._capacity = capacity

    def get(self, i: int) -> int:
        if i < self._size and i >= 0:
            return self._arr[i]
        raise IndexError(f"Index out of bounds (size={self._size}, index={i})")

    def set(self, i: int, n: int) -> None:
        if i < self._size and i >= 0:
            self._arr[i] = n
            return
        raise IndexError(f"Index out of bounds (size={self._size}, index={i})")

    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self._arr[self._size] = n
        self._size += 1

    def popback(self) -> int:
        if self._size > 0:
            self._size -= 1
            return self._arr[self._size]
        raise RuntimeError("Array is empty")

    def resize(self) -> None:
        self._arr.extend([None] * self._capacity)
        self._capacity = len(self._arr)

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity