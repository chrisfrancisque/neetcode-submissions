class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()

        def dfs(startr, startc):
            visited.add((startr, startc))
            count = 1

            directions = [(1,0), (-1, 0), (0,1), (0,-1)]

            for dr, dc in directions:
                r = startr + dr
                c = startc + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    if grid[r][c] == 1 and (r,c) not in visited:
                        count += dfs(r,c)

            return count


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    
                    curr = dfs(i, j)
                    res = max(res, curr)
        
        return res
        