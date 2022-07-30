class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
       
        
        adjList=defaultdict(list) 
        for ind,val in enumerate(manager):
            if(val!=-1):
                adjList[val].append(ind)
         
        
        
        minheap=[[informTime[headID],headID]]
        
        heapq.heapify(minheap)
        visited=set()
        
        
        res=0
        
        while(len(visited)!=n and minheap):
            
            dist,node=heapq.heappop(minheap)
            
            if node in visited:
                continue
               
            visited.add(node)
            res=max(res,dist)
            
            for nei in adjList[node]:
                if nei not in visited:
                    heapq.heappush(minheap,[informTime[nei]+dist,nei])
                   
         
        
        if (len(visited)==n):
            return res
                    
        return -1   
            
            
            
            
            
            
            
            
            
            
            
            
        
        
            
        
       