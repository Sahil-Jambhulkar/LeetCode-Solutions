class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        m={}
        
        for no in nums:           
            if no in m:
                m[no]+=1
            else:
                m[no]=1
                
        lst=[[] for i in range(len(nums)+1)]   
        
        for key,val in m.items():
            lst[val].append(key)
        
        res=[]
        
        
        for elelist in lst[-1:0:-1]:
            for ele in elelist:
                print()
                if k>0:
                    res.append(ele)
                    k-=1
            
                    
        return res   
                
                
                
                
            
            
            
            
            
            
