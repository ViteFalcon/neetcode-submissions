# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def swapPairs(i: int, j: int):
            tmp = pairs[i]
            pairs[i] = pairs[j]
            pairs[j] = tmp

        def quickSortAndGetNewPivot(start: int, end: int):
            pivot = pairs[end]
            i = start - 1 # highest index into the low side
            for j in range(start, end):
                if pairs[j].key < pivot.key:
                    i += 1
                    swapPairs(i, j)
            nextPivotIndex = i + 1
            swapPairs(nextPivotIndex, end)
            return nextPivotIndex

        def quickSortSegment(start: int, end: int):
            if start >= end:
                return
            pivotIndex = quickSortAndGetNewPivot(start, end)
            quickSortSegment(start, pivotIndex - 1)
            quickSortSegment(pivotIndex + 1, end)

        quickSortSegment(0, len(pairs)-1)
        return pairs