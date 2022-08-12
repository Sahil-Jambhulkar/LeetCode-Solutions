class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        intervals.append(newInterval)
        
        sortedInterval=sorted(intervals)
        
        print(sortedInterval)
                
        res=[sortedInterval[0]]
        
        
        for i in range(1,len(sortedInterval)):
            
            if res[-1][1]>=sortedInterval[i][0]:
                res[-1][1]=max(res[-1][1],sortedInterval[i][1])
              
            else:
                print('else')
                res.append(sortedInterval[i])
               
           
        return res
        