class MinHeap:
    
    def __init__(self):
        self._heap = []

    def push(self, val: int) -> None:
        self._heap.append(val)
        self._heapify_up()

    def _swap(self, index1: int, index2: int) -> None:
        temp = self._heap[index1]
        self._heap[index1] = self._heap[index2]
        self._heap[index2] = temp

    def _heapify_up(self) -> None:
        if not self._heap:
            return
        index = len(self._heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self._heap[index] >= self._heap[parent]:
                break
            self._swap(index, parent)
            index = parent

    def _heapify_down(self) -> None:
        index = 0
        while index < len(self._heap):
            value = self._heap[index]
            left = 2 * index + 1
            right = 2 * index + 2
            left_value = self._heap[left] if left < len(self._heap) else float('inf')
            right_value = self._heap[right] if right < len(self._heap) else float('inf')
            if left_value < value and left_value < right_value:
                self._swap(index, left)
                index = left
            elif right_value < value:
                self._swap(index, right)
                index = right
            else:
                break

    def top(self) -> int:
        return self._heap[0] if self._heap else -1

    def pop(self) -> int:
        if not self._heap:
            return -1
        result = self._heap[0]
        last_value = self._heap.pop()
        if len(self._heap) >= 1:
            self._heap[0] = last_value
        self._heapify_down()
        return result

    def heapify(self, nums: list[int]) -> None:
        self._heap.clear()
        for n in nums:
            self.push(n)
