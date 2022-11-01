class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        cache = [0]*(n+1)
        
        for i in range(1,n+1):
            curmax = 0
            for j in range(1,min(k,i)+1):
                curmax = max(curmax,arr[i-j])
                cache[i] = max(cache[i],cache[i-j] + (curmax*j))
        
        return cache[n]
            