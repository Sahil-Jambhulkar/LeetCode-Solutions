class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lowerString = s.lower()
        
        
        finalString=''
        
        for ch in lowerString:
            if ch.isalnum():
                finalString+=ch
        
        
        l=0
        r=len(finalString)-1
        
        while(l<=r):
            if finalString[l]!=finalString[r]:
                return False
            l+=1
            r-=1
        
        
        return True
            
            
            
            
            
                
            
        