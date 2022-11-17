class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        m = {}
        
        for index,number in enumerate(nums):
            
            othernumber = target - number
            
            if othernumber in m:
                return [m[othernumber],index]
            
            else:
                m[number] = index
                
                
            
        
        
        