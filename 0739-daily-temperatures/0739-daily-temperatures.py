class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0 for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            curtemp = temperatures[i]
            while len(stack) and curtemp >= stack[-1][0]:
                stack.pop()
            if len(stack):
                res[i] = stack[-1][1]-i
            stack.append([curtemp,i])
        
        return res
            
                