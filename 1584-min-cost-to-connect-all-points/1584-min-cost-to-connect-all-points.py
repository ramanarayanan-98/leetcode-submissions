class Solution:
    def find(self,par,x):
        if par[x] != x:
            par[x] = self.find(par,par[x])
        return par[x]
    def union(self,par,rank,xlead,ylead)->bool:
        if xlead == ylead:
            return False
        if rank[xlead] >= rank[ylead]:
            par[ylead] = xlead
            rank[xlead] += rank[ylead]
        else:
            par[xlead] = ylead
            rank[ylead] += rank[xlead]
        return True
            
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        par = list(range(n))
        rank = [1 for _ in range(n)]
        minheap = []
        
        for i in range(n-1):
            for j in range(i+1,n):
                x1,y1,x2,y2 = points[i][0],points[i][1],points[j][0],points[j][1]
                minheap.append([abs(x1-x2)+abs(y1-y2),i,j])
        
        heapq.heapify(minheap)
        cost = 0
        while len(minheap):
            edge = heapq.heappop(minheap)
            i,j = edge[1],edge[2]
            i,j = self.find(par,i),self.find(par,j)
            if self.union(par,rank,i,j):
                cost += edge[0]
                if rank[i] == n or rank[j] == n:
                    break
            
        return cost
            
            
            
            
        