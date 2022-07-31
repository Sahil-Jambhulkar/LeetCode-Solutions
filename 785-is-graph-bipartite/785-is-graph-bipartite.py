class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        
        
        def dfs(i,color):
            if i in colors:
                return not colors[i]==color
            
            colors[i]=color
            
            for nei in graph[i]:
                    if dfs(nei,1-color):
                        return True
            
            
        
        colors={}
        
        for i in range(len(graph)):
            if i not in colors:
                if dfs(i,0):
                    return False
                
           
        return True
        