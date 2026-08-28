class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        island = 0

        def dfs(start_r, start_c):
            visited.add((start_r, start_c))
            directions = [[1,0], [-1, 0], [0,-1], [0,1]]

            for dr, dc in directions:
                r = start_r + dr
                c = start_c + dc

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited and grid[r][c] =='1':
                    dfs(r,c)





        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i, j)
                    island += 1
        
        return island
        









        