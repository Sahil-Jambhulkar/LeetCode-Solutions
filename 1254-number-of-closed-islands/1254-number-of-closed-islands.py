class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])
        
        def noisland(r,c):
            visited.add((r,c))
            
            direction=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in direction:
                row=r+dr
                col=c+dc
                
                if(row in range(rows) and col in range(cols) and grid[row][col]==0 and (row,col) not in visited):
                    noisland(row,col)
            
        
        
        def dfs(r,c):
            grid[r][c]=1
            
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            
            for dr,dc in directions:
                row=r+dr
                col=c+dc
                
                if(row in range(rows) and col in range(cols) and grid[row][col]==0):
                    dfs(row,col)
        
        
        for r in range(rows):
            if grid[r][0]==0:
                dfs(r,0)
               
            if grid[r][cols-1]==0:
                dfs(r,cols-1)
            
        for c in range(cols):
            if grid[0][c]==0:
                dfs(0,c)
               
            if grid[rows-1][c]==0:
                dfs(rows-1,c)      
        
           
        count=0
        visited=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0 and (r,c) not in visited:
                    noisland(r,c)
                    count+=1
           
        return count
                   
              
           
        
        
        
        