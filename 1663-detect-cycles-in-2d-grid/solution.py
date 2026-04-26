class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        elements = set()
        for subList in grid:
            for element in subList:
                elements.add(element)
        
        global already_gone
        global x_len
        global y_len
        global grid1

        already_gone = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        x_len = len(grid[0])
        y_len = len(grid)
        grid1 = grid

        for y, subList in enumerate(grid):
            for x, val in enumerate(subList):
                if not already_gone[y][x] and self.dfs(x, y, val, (x, y)):
                    
                    return True

        return False



    def dfs(self, x, y, val, start, last_pos = (-1, -1)):
        if already_gone[y][x]:
            return True
        else:
            already_gone[y][x] = True
        ans = []

        if x != 0 and grid1[y][x - 1] == val and last_pos != (x - 1, y):
            ans.append(self.dfs(x - 1, y, val, start, (x, y)))
        if y != 0 and grid1[y - 1][x] == val and last_pos != (x, y - 1):
            ans.append(self.dfs(x, y - 1, val, start, (x, y)))
        if x != x_len - 1 and grid1[y][x + 1] == val and last_pos != (x + 1, y):
            ans.append(self.dfs(x + 1, y, val, start, (x, y)))
        if y != y_len - 1 and grid1[y + 1][x] == val and last_pos != (x, y + 1):
            ans.append(self.dfs(x, y + 1, val, start, (x, y)))

        if ans.count(True):
            return True
        return False


            
                


                
                    



