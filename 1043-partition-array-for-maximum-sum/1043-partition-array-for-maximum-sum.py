class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        cache = [0]*k
        
        for i in range(1,n+1):
            curmax,best = 0,0
            for j in range(1,min(k,i)+1):
                curmax = max(curmax,arr[i-j])
                best = max(best,cache[(i-j)%k] + (curmax*j))
            cache[i%k] = best
        
        return cache[n%k]
            