class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        
        def dfs(i):
            visited.add(i)
            
            for nei in rooms[i]:
                if nei not in visited:
                    dfs(nei)
                   
        
        visited=set()
        dfs(0)
        
        if(len(visited)==len(rooms)):
            return True
        
        return False
        
        
        
        
        
        