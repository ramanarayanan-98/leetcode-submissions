class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        i = 0
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        if i == len(intervals):
            res.append(newInterval)
            return res
        else:
            res.append([min(newInterval[0],intervals[i][0]),newInterval[1]])
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            i += 1
        
        if i > 0:
            res[-1][1] = max(res[-1][1],intervals[i-1][1])
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
            