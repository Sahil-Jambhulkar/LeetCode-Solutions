class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            
            visited.add(i)
            
            for ind,val in enumerate(isConnected[i]):
                if val==1 and ind not in visited:
                    dfs(ind)
        
        
        
        visited=set()
        count=0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count+=1
           
        return count
        