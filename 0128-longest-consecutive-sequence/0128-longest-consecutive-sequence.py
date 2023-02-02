class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        res=0
        nums=set(nums)
        
        for no in nums:
            
            if no-1 not in nums:
                
                k=1
                while((no+1) in nums):
                    k+=1
                    no+=1
                   
                res=max(res,k)
        
        return res
            
           