class Solution:
    def eucDist(self,point):
        return -((point[0]**2 + point[1]**2)**0.5)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        
        for point in points:
            if len(maxheap) < k:
                heapq.heappush(maxheap,[self.eucDist(point),point])
            else:
                heapq.heappushpop(maxheap,[self.eucDist(point),point])
        
        return [maxheap[i][1] for i in range(k)]
        
        