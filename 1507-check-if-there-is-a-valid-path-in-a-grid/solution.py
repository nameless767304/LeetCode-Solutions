class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        
        y_max = len(grid)   
        x_max = len(grid[0]) 
        direction_info = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1) }
        direction = {1: (1, 2), 2: (3, 4), 3: (1, 4), 4: (2, 4), 5: (1, 3), 6: (2, 3)} 

        grid_info = [[set() for _ in range(x_max)] for _ in range(y_max)] 
        visited = set()



        def dfs(x, y):
            if (x, y) in visited:
                return False

            if x == x_max - 1 and y == y_max - 1:
                return True 

            for info in grid_info[y][x]:
                dx, dy = info[0], info[1]
                if x + dx >= 0 and x + dx < x_max and y + dy >= 0 and y + dy < y_max:
                    visited.add((x, y))
                    if (-dx, -dy) in grid_info[y + dy][x + dx]:
                        if dfs(x + dx, y + dy):
                            return True
            return False

        for y, subgrid in enumerate(grid):
            for x, val in enumerate(subgrid):
                for info in direction[val]:
                    grid_info[y][x].add(direction_info[info])

        return dfs(0, 0)



