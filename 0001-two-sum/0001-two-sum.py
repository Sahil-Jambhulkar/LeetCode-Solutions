class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m={}
        
        
        for index,number in enumerate(nums):
            altNo=target-number
            
            if altNo in m:
                return [m[altNo],index]
            
            else:
                m[number] = index
                
            
            
            
        
     