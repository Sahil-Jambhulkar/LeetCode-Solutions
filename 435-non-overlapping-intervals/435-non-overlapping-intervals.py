class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        intervals=sorted(intervals)
        res=[]
        
        res.append(intervals[0])
        
        count=0
        for i in range(1,len(intervals)):
            
            if res[-1][1]>intervals[i][0]:
                count+=1
                
                
                if intervals[i][1]<=res[-1][1]:
                    res[-1][0]=intervals[i][0]
                    res[-1][1]=intervals[i][1]
                   
                
            else:
                res.append(intervals[i])
    
        return count
       