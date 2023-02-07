class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        stack=[]
        
        stack.append(prices[-1])
        
        res=0
        for i in range(len(prices)-2,-1,-1):
            if stack[-1]<=prices[i]:
                stack.append(prices[i])
            else:
                ans=stack[-1]-prices[i]
                res=max(res,ans)
            
        return res
            
        
        
       