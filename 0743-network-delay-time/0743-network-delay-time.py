class Solution:
    def dijikstra(self,adjmat,dist,k,n,visited):
        minheap = []
        heapq.heappush(minheap,[dist[k-1],k-1])
        
        while len(minheap):
            curdist,curnode = heapq.heappop(minheap)
            
            visited.add(curnode)
            
            for nei in adjmat[curnode]:
                if nei in visited:
                    continue
                
                olddist = dist[nei]
                newdist = curdist + adjmat[curnode][nei]
                
                if newdist < olddist:
                    heapq.heappush(minheap,[newdist,nei])
                    dist[nei] = newdist
            
            
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjmat = [dict() for _ in range(n)]
        
        for time in times:
            adjmat[time[0]-1][time[1]-1] = time[2]
        
        dist = [float("inf") for _ in range(n)]
        
        dist[k-1] = 0
        visited = set()
        
        self.dijikstra(adjmat,dist,k,n,visited)
        
        return max(dist) if max(dist) != float(inf) else -1