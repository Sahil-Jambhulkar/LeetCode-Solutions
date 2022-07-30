class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows=len(mat)
        cols=len(mat[0])
        
        ans=[]
        q=collections.deque()
        
        for r in range(rows):
            temp=[]
            for c in range(cols):
                temp.append(-1)
              
            ans.append(temp)
           
       
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    q.append((r,c))
                    ans[r][c]=0
                   
               
        
        while(q):
            
            r,c=q.popleft()
            
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            
            for dr,dc in directions:
                row=r+dr
                col=c+dc
                
                if(row in range(rows) and col in range(cols) and ans[row][col]==-1):
                    ans[row][col]=ans[r][c]+1
                    q.append((row,col))
                   
               
           
        return ans
                   
               
           
        
        
        
        
        
            
                
        
            
        
        
        