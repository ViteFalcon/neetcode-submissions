class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1:
            return -1
        R, C = len(grid), len(grid[0])
        if grid[R - 1][C - 1] == 1:
            return -1
        queue = deque([(0, 0, 0)])  # (row, col, distance)
        visited = {(0, 0)}
        end_position = (R - 1, C - 1)

        while queue:
            r, c, dist = queue.popleft()
            if (r, c) == end_position:
                return dist
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                pos = (nr, nc)
                if 0 <= nr < R and 0 <= nc < C and pos not in visited and grid[nr][nc] == 0:
                    visited.add(pos)
                    queue.append((nr, nc, dist + 1))
        return -1