class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        l=[]
        for ch in s:
            if ch in l:
                return ch
            else:
                l.append(ch)
               
           
        
        
        