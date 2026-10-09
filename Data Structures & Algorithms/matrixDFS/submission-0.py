
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[m - 1][n - 1] != 0:
            return 0
        
        visited = set()
        
        def dfs(r: int, c: int) -> int:
            if r == m - 1 and c == n - 1:
                return 1
            visited.add((r, c))
            count = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    count += dfs(nr, nc)
            visited.remove((r, c))
            return count
            
        return dfs(0, 0)