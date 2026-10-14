import heapq

from collections import defaultdict

INFINITY = float('inf')

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph : dict[dict[int,int]] = {}
        for edge in edges:
            source, dest, distance = edge
            if source not in graph:
                graph[source] = {}
            if dest not in graph[source] or distance < graph[source][dest]:
                graph[source][dest] = distance
            if dest not in graph:
                # Make sure that all nodes exists as keys in the graph
                graph[dest] = {}

        unvisited = set(graph.keys())
        dist = {}
        dist[src] = 0

        def make_queue():
            q_ = [(dist.get(v, INFINITY), v) for v in unvisited]
            if q_:
                heapq.heapify(q_)
            return q_
        
        queue = make_queue()
        while queue:
            distance_from_src, v_curr = heapq.heappop(queue)
            if distance_from_src == INFINITY:
                break
            edges_v = graph[v_curr]
            for v_dst, distance in edges_v.items():
                distance_min_curr = dist.get(v_dst, INFINITY)
                if distance_from_src + distance < distance_min_curr:
                    dist[v_dst] = distance_from_src + distance
            unvisited.remove(v_curr)
            queue = make_queue()

        return {vertex: dist.get(vertex, -1) for vertex in range(n)}
