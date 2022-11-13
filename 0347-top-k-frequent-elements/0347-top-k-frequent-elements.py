class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = collections.Counter(nums)
        minheap = []
        for num in numsCount:
            if len(minheap) == k:
                heapq.heappushpop(minheap,[numsCount[num],num])
            else:
                heapq.heappush(minheap,[numsCount[num],num])
        
        return [val[1] for val in minheap]