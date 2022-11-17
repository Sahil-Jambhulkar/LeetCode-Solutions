class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    
        m={}
        
        for word in strs:
            
            ascword = sorted(word)
            joinedword =  ''.join(ascword)
            
            if joinedword not in m:
                m[joinedword] = []
            m[joinedword].append(word)
            
        
        
        res = []
        for k,v in m.items():
            res.append(v)
          
        return res
            
             
        
        
      
              
        
        
          
        
        
            
            
            
        