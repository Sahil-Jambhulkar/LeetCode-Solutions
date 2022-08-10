class Solution:
    def frequencySort(self, s: str) -> str:
        
        m={}
        
        for ch in s:
            if ch in m:
                m[ch]+=1
               
            else:
                m[ch]=1
               
           
        q=[]
        
        for ch in m:
            q.append([-1*m[ch],ch])
            
        heapq.heapify(q)
        ans=''
        while(q):
            freq,ch=heapq.heappop(q)
            ans+=ch*(freq*-1)
           
        return ans
            
            
           
        
            
        