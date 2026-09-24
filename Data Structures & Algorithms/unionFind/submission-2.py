class UnionFind:
    
    def __init__(self, n: int):
        self._components: dict[int, set[int]] = {
            i: set([i]) for i in range(n)
        }
        self._mapping: dict[int, int] = {
            k:k for k in range(n)
        }

    def find(self, x: int) -> int:
        return self._mapping.get(x, -1)

    def isSameComponent(self, x: int, y: int) -> bool:
        ix = self.find(x)
        iy = self.find(y)
        if ix == -1 or iy == -1:
            return False
        return ix == iy

    def union(self, x: int, y: int) -> bool:
        ix = self.find(x)
        if ix == -1:
            return False
        iy = self.find(y)
        if iy == -1 or ix == iy:
            return False
        cy = self._components[iy]
        del self._components[iy]
        self._components[ix] |= cy
        self._mapping |= {c:ix for c in cy}
        return True

    def getNumComponents(self) -> int:
        return len(self._components)
