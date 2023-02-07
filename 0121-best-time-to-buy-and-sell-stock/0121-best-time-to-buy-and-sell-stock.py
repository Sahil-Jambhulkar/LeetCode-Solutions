class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l=0
        r=0
        res=0
        nums=prices
        
        while(r<len(prices)):
            
            if nums[r]<nums[l]:
                l=r
                
            else:
                res=max(res,nums[r]-nums[l])
                
            r+=1
        
        
        
        return res