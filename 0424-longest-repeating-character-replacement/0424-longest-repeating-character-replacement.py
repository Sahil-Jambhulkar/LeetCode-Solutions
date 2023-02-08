class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        m = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            
            m[s[r]] = 1 + m.get(s[r],0)
            
            if(r-l+1 - max(m.values()) > k):
                
                m[s[l]]-=1
                l+=1
                
            res = max(res,r-l+1)
        
        return res
        