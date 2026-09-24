class Graph:
    
    def __init__(self):
        self._edges: dict[int, int] = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self._edges[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        can_delete_edge =  src in self._edges and dst in self._edges[src]
        if can_delete_edge:
            self._edges[src].remove(dst)
        return can_delete_edge


    def hasPath(self, src: int, dst: int) -> bool:
        visited: set[int] = set()
        nodes = deque([src])
        while nodes:
            node = nodes.popleft()
            if node in visited:
                continue
            if dst in self._edges[node]:
                return True
            visited.add(node)
            for n in self._edges[node]:
                if n not in visited and n in self._edges:
                    nodes.append(n)
        return False
