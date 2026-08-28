class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        visited = set()
        island = 0


        def bfs(r_start, c_start):
            visited.add((r_start, c_start))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            for dx, dy in directions:
                r = r_start + dx
                c = c_start + dy
                print(r,c)

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                     if (r,c) not in visited and grid[r][c] == '1':
                        bfs(r,c)
            



        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j] == '1':
                    bfs(i,j)
                    island +=1 
        
        return island
        