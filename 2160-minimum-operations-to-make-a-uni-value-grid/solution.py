class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid_1d = []
        remainder = grid[0][0] % x
        ans = 0

        for subgrid in grid:
            for num in subgrid:
                if num % x != remainder:
                    return -1
        
            grid_1d.extend(subgrid)

        grid_1d.sort()
        criteria = grid_1d[len(grid_1d) // 2]

        for num in grid_1d:
            ans += abs(num - criteria) // x

        return ans
