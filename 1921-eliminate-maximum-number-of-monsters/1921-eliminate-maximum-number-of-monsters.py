class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        
        time = [] 
        
        for i in range(len(speed)):
            time.append(math.ceil(dist[i]/speed[i]))
        time.sort()
        
        res=0
        
        for minute in range(len(time)):
            if minute>=time[minute]:
                return res
            res+=1
           
        return res