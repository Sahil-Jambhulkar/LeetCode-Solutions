class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        
        
        r=len(numbers)-1
        l=0
        
        while(l<r):
            total = numbers[l]+numbers[r]
            if total== target :
                return [l+1,r+1]
            
            elif total<target:
                l+=1
               
            else:
                r-=1
    
        
        
        