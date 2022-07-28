class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        def dfs(node):
            
            res.append(node)
            if(node==len(graph)-1):
                ans.append(res[:])
            
            else:
                for nei in graph[node]:
                        dfs(nei)
            
            res.remove(node) 
        
        res=[]
        ans=[]
        
      
        dfs(0)
            
        return ans
        
