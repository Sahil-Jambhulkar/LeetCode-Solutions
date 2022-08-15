class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        
        time = [] 
        
        
        for i in range(len(speed)):
            time.append(dist[i]/speed[i]) 
        time.sort()
        
        
        
        
        for i in range(len(time)): #t is also the current time
            reached = (time[i] - i <= 0)
            if reached : 
                return i 
            
        return len(time) 