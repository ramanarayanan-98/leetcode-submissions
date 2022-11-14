class Solution:
    def dfs(self,heights,visited,ci,cj,fm):
        
        if visited[ci][cj]:
            return
        
        visited[ci][cj] = True
        fm[ci][cj] = 1
        
        curval = heights[ci][cj]
        
        if ci > 0 and heights[ci-1][cj] >= heights[ci][cj]:
            self.dfs(heights,visited,ci-1,cj,fm)
        if cj > 0 and heights[ci][cj-1] >= heights[ci][cj]:
            self.dfs(heights,visited,ci,cj-1,fm)
        if ci < len(heights)-1 and heights[ci+1][cj] >= heights[ci][cj]:
            self.dfs(heights,visited,ci+1,cj,fm)
        if cj < len(heights[0])-1 and heights[ci][cj+1] >= heights[ci][cj]:
            self.dfs(heights,visited,ci,cj+1,fm)
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m,n = len(heights),len(heights[0])
        pacificFlowMat = [[0 for _ in range(n)]for _ in range(m)]
        atlanticFlowMat = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            pacificFlowMat[i][0] = 1
            atlanticFlowMat[i][n-1] = 1
        
        for j in range(n):
            pacificFlowMat[0][j] = 1
            atlanticFlowMat[m-1][j] = 1
            
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if pacificFlowMat[i][j] == 1:
                    self.dfs(heights,visited,i,j,pacificFlowMat)
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if atlanticFlowMat[i][j] == 1:
                    self.dfs(heights,visited,i,j,atlanticFlowMat)
        
        res = []
        for i in range(m):
            for j in range(n):
                if pacificFlowMat[i][j] == 1 and atlanticFlowMat[i][j] == 1:
                    res.append([i,j])
        
        return res
        
        
        
                
        
        