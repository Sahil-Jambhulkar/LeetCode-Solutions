class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        rows=len(accounts)
        cols=len(accounts[0])
        
        res=-math.inf
        
        for r in range(rows):
            total=0
            for c in range(cols):
                total+=accounts[r][c]
                
            if(total>res):
                res=total
               
            
        return res 
                
                
        