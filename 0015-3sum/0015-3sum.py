class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums=sorted(nums)
        print(nums)
        
        res=[]
        
        for i in range(len(nums)):
            
            if(i>0 and nums[i-1]==nums[i]):
                continue
            l=i+1   
            r = len(nums)-1
            
            while(l<r):
                total= nums[i]+nums[l]+nums[r]
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                
                else:            
                    res.append([nums[l],nums[i],nums[r]])
                    l+=1
                    
                    while(nums[l-1]==nums[l] and l<r):
                        l+=1
                    
        return(res)
                    
                    
                    
                    
                    
        
                
                
                
                
                
        