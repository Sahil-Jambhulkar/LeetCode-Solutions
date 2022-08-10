class Solution:
    def frequencySort(self, s: str) -> str:
        
        #Bucket Sort Implementation 
        #T.C-> O(N)
        #S.C-> O(N)
        
        m={}
        
        for ch in s:
            if ch in m:
                m[ch]+=1
            else:
                m[ch]=1
          
        l=[[]  for i in range(len(s)+1)]

        
        for key,val in m.items():
            l[val].append(key)
            
        res=''
        
        for i in range(len(l)-1,-1,-1):
            for ch in l[i]:
                res+=ch*i
               
        return res
                
            
