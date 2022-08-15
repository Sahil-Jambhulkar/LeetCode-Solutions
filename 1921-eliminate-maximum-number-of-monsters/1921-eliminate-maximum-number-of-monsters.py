class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        
        time = [0]*len(dist) 
        
        
        for i in range(len(speed)):
            time[i]=dist[i]/speed[i]
        time.sort()
        
        
        for i in range(len(time)):
            reached = (time[i] - i <= 0)
            if reached : 
                return i 
            
        return len(time) 