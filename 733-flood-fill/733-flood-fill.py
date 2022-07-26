class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        rows=len(image)
        cols=len(image[0])
        
        visited=set()
        sourceColor=image[sr][sc]
        
        if sourceColor==newColor:
            return image
        
        def dfs(r,c,newColor,sourceColor):
            visited.add((r,c))
            image[r][c]=newColor
            
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            
            for dr,dc in directions:
                row=r+dr
                col=c+dc
                
                if(row in range(rows) and col in range(cols) and (row,col) not in visited and image[row][col]==sourceColor):
                    dfs(row,col,newColor,sourceColor)
                    
        
        for r in range(rows):
            for c in range(cols):
                    dfs(sr,sc,newColor,sourceColor)
           
        return image
            
        
        
        
        
        
        
       