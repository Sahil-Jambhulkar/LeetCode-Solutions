class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        
        time = [] 
        
        
        for i in range(len(speed)):
            time.append(dist[i]/speed[i])
        time.sort()
        
        print(time)
        for i in range(len(time)):
            reached = (time[i] - i <= 0)
            print(reached)
            if reached : 
                print('asdas')
                return i 
            
        return len(time) 