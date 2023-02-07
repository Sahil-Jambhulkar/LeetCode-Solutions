class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        charset=set()
        
        res=0
        
        while(r<len(s)):
            
            while(s[r] in charset):
                charset.remove(s[l])
                l+=1
            
            res=max(res,r-l+1)
            charset.add(s[r])
            r+=1
        
        return res
        
        
        
      