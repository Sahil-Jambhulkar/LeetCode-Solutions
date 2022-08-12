class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        sortedInt=sorted(intervals)

        res=[]
        print(sortedInt)
        res.append(sortedInt[0])
        
        for i in range(1,len(sortedInt)):
            if res[-1][1]>=sortedInt[i][0]:
                res[-1][1]=max(res[-1][1],sortedInt[i][1])
            else:
                res.append(sortedInt[i])
           
        return res
            
        