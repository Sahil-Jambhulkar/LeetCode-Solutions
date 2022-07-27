class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #MST so we will ise prism algorithm
        
        adjList={i:[] for i in range(len(points))}
        
        
        for i in range(len(points)):
            x1,y1=points[i]
            
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                
                distance=abs(x1-x2)+abs(y1-y2)
                adjList[i].append([distance,j])
                adjList[j].append([distance,i])
               
           
        minheap=[]
        heapq.heapify(minheap)
        
        minheap.append([0,0])
        
        visited=set()
        res=0
        
        while(len(visited)!=len(points)):
            distance,node=heapq.heappop(minheap)

            if node in visited:
                continue
            visited.add(node)
            res+=distance
            
            for distance,nei in adjList[node]:
                if nei not in visited:
                    heapq.heappush(minheap,[distance,nei])

            
        return res 
            
            
            
            
            
            
        
        
        