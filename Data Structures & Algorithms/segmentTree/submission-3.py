class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self._sums = list(nums)
        for i in range(1,len(nums)):
            self._sums[i] += self._sums[i-1]

    def update(self, index: int, val: int) -> None:
        # [1, 2, 3] > [1, 3, 6]
        # [1, 0, 3] > [1, 1, 4]
        parent_sum = 0 if index == 0 else self._sums[index-1]
        prev_val = self._sums[index] - parent_sum
        val_diff = val - prev_val
        self._sums[index] = val + parent_sum
        for i in range(index + 1, len(self._sums)):
            self._sums[i] += val_diff
    
    def query(self, L: int, R: int) -> int:
        l_sum = 0 if L == 0 else self._sums[L-1]
        return self._sums[R] - l_sum
