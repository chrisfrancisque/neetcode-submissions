class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def bfs(startr, startc):
            visited.add((startr, startc))
            
            directions = [(1,0), (-1,0), (0,1), (0,-1) ]
            for dr, dc in directions:
                r = startr + dr
                c = startc + dc
                if 0<= r < len(grid) and 0<= c < len(grid[0]):
                    if  grid[r][c] == '1' and (r,c) not in visited:
                        bfs(r,c)




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    islands +=1 
        
        return islands
        