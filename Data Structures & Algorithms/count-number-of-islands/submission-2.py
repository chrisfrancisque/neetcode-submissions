class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        islands = 0
        visited = set()


        def dfs(start_r, start_c):
            visited.add((start_r, start_c))

            directions = [[1,0], [-1,0], [0, 1], [0, -1]]

            for dx, dy in directions:
                r = start_r + dx
                c = start_c + dy
                print(r, c)
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    if grid[r][c] == '1' and (r,c) not in visited:
                        dfs(r,c)

            



        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1
        
        return islands





        