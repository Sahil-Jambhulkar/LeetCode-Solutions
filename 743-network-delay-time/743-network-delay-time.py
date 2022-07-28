class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        adjList={i:[] for i in range(1,n+1)}
        
        
        for st,end,distance in times:
            adjList[st].append([distance,end])
            
          
        minheap=[[0,k]]
        
        heapq.heapify(minheap)
        visited=set()
        
        
        res=0
        
        while(len(visited)!=n and minheap):
            
            dist,node=heapq.heappop(minheap)
            
            if node in visited:
                continue
               
            
            visited.add(node)
            res=max(res,dist)
            
            for neiDist,nei in adjList[node]:
                if nei not in visited:
                    heapq.heappush(minheap,[neiDist+dist,nei])
                   
         
        
        if (len(visited)==n):
            return res
                    
        return -1   
            
            
            
            
            
            
            
            
            
            
            
            
        
        
            
        
       