class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0]) 
        
        
        
        
        def dfs(r,c):
            grid[r][c]=2
            
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            
            for dr,dc in directions:
                row=r+dr
                col=c+dc
                
                if(row in range(rows) and col in range(cols) and grid[row][col]==1):
                    dfs(row,col)
                
            
        
        for c in range(cols):
            if grid[0][c]==1:
                dfs(0,c)
            if grid[rows-1][c]==1:
                dfs(rows-1,c)
               
            
        for r in range(rows):
            if grid[r][0]==1:
                dfs(r,0)
            if grid[r][cols-1]==1:
                dfs(r,cols-1)
        
        
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    count+=1
        
        return count
        
        
        
        
        
        
        
        