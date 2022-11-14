class Solution:
    def dijikstra(self,adjmat,dist,k,n,visited):
        minheap = []
        heapq.heappush(minheap,[dist[k-1],k-1])
        
        while len(minheap):
            curdist,curnode = heapq.heappop(minheap)
            
            visited.add(curnode)
            
            for i in range(len(adjmat)):
                if i in visited:
                    continue
                if adjmat[curnode][i] == float("inf"):
                    continue
                olddist = dist[i]
                newdist = curdist + adjmat[curnode][i]
                
                if newdist < olddist:
                    heapq.heappush(minheap,[newdist,i])
                    dist[i] = newdist
            
            
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjmat = [[float(inf) for _ in range(n)]for _ in range(n)]
        for i in range(n):
            adjmat[i][i] = 0
        
        for time in times:
            adjmat[time[0]-1][time[1]-1] = time[2]
        
        dist = [float("inf") for _ in range(n)]
        
        dist[k-1] = 0
        visited = set()
        
        self.dijikstra(adjmat,dist,k,n,visited)
        
        return max(dist) if max(dist) != float(inf) else -1