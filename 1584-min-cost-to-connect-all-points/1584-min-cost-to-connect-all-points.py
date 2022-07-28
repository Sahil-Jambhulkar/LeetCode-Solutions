class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #MST so we will USE PRISM algorithm
        
        
        adjList={i:[] for i in range(len(points))}
        
        for i in range(len(points)):
            x1,y1=points[i]
            
            for j in range(len(points)):
                x2,y2=points[j]
                distance=abs(x1-x2)+abs(y1-y2)
                adjList[i].append([distance,j])
                adjList[j].append([distance,i])
                
            
        q=[[0,0]]
        
        heapq.heapify(q)
        visited=set()
        res=0
        
        while(len(visited)!=len(points)):
            
            dist,node=heapq.heappop(q)
            
            if node in visited:
                continue
               
            res+=dist
            visited.add(node)
            
            for diss,nei in adjList[node]:
                if nei not in visited:
                    heapq.heappush(q,[diss,nei])
                   
        
        return res
                    
               
            

          
        
        
       