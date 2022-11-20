class DSU:
    def __init__(self):
        self.parent = list(range(1001))
        self.rank = [0 for _ in range(1001)]
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,a,b) -> bool:
        a_lead,b_lead = self.find(a),self.find(b)
        
        if a_lead == b_lead:
            return False
        
        if self.rank[a_lead] > self.rank[b_lead]:
            self.parent[b_lead] = a_lead
        elif self.rank[b_lead] > self.rank[a_lead]:
            self.parent[a_lead] = b_lead
        else:
            self.rank[a_lead] += 1
            self.parent[b_lead] = a_lead
        return True
        
class Solution:
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
        
        return [-1,-1]
            
        
        