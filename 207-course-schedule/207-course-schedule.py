class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList={i:[]  for i in range(numCourses)}
        
        for c,p in prerequisites:
            adjList[c].append(p)
        
        def dfs(i):
            visited.add(i)
            dfsvisited.add(i)
            
            for nei in adjList[i]:
                if nei not in visited:
                    if(dfs(nei)):
                        return True
                elif nei in dfsvisited:
                    return True
            dfsvisited.remove(i)
        visited=set()
        dfsvisited=set()
        
        for i in adjList:
            if i not in visited:
                if(dfs(i)):
                    return False
           
        return True
            
        
      