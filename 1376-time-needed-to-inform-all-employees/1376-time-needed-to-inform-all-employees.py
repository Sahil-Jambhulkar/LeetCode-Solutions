class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        
        if n==1:
            return 0
        
        adjList=defaultdict(list) 
        for ind,val in enumerate(manager):
            if(val!=-1):
                adjList[val].append(ind)
           
        print(adjList)
        
        
        q=collections.deque()
        
        q.append([headID,informTime[headID]])
        
        res=0
        
        while(q):
            
            for i in range(len(q)):
                node,ift=q.popleft()
                res = max(res,ift)
               
                for nei in adjList[node]:
                    q.append([nei,informTime[nei]+ift])
            
            
        
        return res
            
        
        
        
        
        
        
            
        
        
        
        
        
        
        