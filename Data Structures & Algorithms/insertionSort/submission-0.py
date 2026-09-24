# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []

        def clone_pairs(p: List[Pair]):
            return [Pair(i.key, i.value) for i in p]

        pairs = clone_pairs(pairs)
        states = [pairs]

        for i in range(1, len(pairs)):
            pairs = clone_pairs(states[-1])
            j = i
            while j > 0 and pairs[j-1].key > pairs[j].key:
                 tmp = pairs[j]
                 pairs[j] = pairs[j-1]
                 pairs[j-1] = tmp
                 j -= 1
            states.append(pairs)
        return states