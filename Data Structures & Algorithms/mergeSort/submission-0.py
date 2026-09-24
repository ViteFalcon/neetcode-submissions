# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

def pair_repr(self: Pair) -> str:
    return f'{{{self.key}:"{self.value}"}}'

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return []
        
        def sortAndMerge(left_side: List[Pair], right_side: List[Pair]):
            merged = []
            i = j = 0

            while i < len(left_side) and j < len(right_side):
                if left_side[i].key <= right_side[j].key:
                    merged.append(left_side[i])
                    i += 1
                else:
                    merged.append(right_side[j])
                    j += 1

            merged.extend(left_side[i:])
            merged.extend(right_side[j:])
            return merged

        def divideAndMerge(left, right):
            if left == right:
                return [pairs[right]]

            if left > right:
                return []

            mid = (left + right) // 2

            left_half = divideAndMerge(left, mid)
            right_half = divideAndMerge(mid + 1, right)
            return sortAndMerge(left_half, right_half)

        return divideAndMerge(0, len(pairs)-1)
