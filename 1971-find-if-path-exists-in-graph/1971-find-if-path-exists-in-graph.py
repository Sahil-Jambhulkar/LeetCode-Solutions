class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adjList={i:[] for i in range(n)}
        
        for x,y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
           
        print(adjList)
        
        visited=set()
            
        def dfs(node):
            if node==destination:
                return True
            visited.add(node)
            
            for nei in adjList[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
                   
               
           
        for i in adjList:
            if i not in visited:
                if dfs(source):
                    return True
           
        return False
            
        
        