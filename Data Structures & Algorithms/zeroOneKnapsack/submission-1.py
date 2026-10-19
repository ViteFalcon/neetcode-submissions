class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [[-1 for _ in range(M+1)] for _ in range(N)]
        def dfs(i, capacity_i):
            if i >= len(profit):
                return 0
            if cache[i][capacity_i] != -1:
                return cache[i][capacity_i]

            max_profit = dfs(i + 1, capacity_i)

            new_capacity = capacity_i - weight[i]
            if new_capacity >= 0:
                p = profit[i] + dfs(i + 1, new_capacity)
                max_profit = max(p, max_profit)
            cache[i][capacity_i] = max_profit
            return max_profit
        return dfs(0, capacity)
