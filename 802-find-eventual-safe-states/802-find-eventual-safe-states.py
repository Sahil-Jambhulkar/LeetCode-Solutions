class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visited=set()
        dfsvisited=set()
        
        def dfs(node,visited,incycle):
            visited.add(node)
            dfsvisited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    if (dfs(nei,visited,incycle)):
                        incycle.add(node)       #here dfs will continue and last node of that cycle is added first (similar to last node in remove in dfsvisited and  also similar to last node is inserted first to stack in toposort)
                        return True
                 
                elif nei in dfsvisited:
                    
                    incycle.add(node)
                    return True
               
            dfsvisited.remove(node)
        
        incycle=set()
        
        for i in range(len(graph)):
            if i not in visited:
                dfs(i,visited,incycle)
               
        ans=[]
        print(incycle)
        
        for i in range(len(graph)):
            if i not in incycle:
                ans.append(i)
           
        return ans
        
                