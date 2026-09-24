class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self._nums = list(nums)

    def update(self, index: int, val: int) -> None:
        self._nums[index] = val
    
    def query(self, L: int, R: int) -> int:
        result = 0
        for i in range(L, R+1):
            result += self._nums[i]
        return result
