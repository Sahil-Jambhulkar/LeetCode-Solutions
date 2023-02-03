class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        l = 0
        r = len(height)-1
        
        res= -math.inf
        
        while(l<r):
            ans = min(height[l],height[r])* (r-l)
            res=max(res,ans)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return res
            
            
        
        
        