class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOranges = set()
        rottenOranges = deque()
        m,n = len(grid),len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rottenOranges.append(tuple([i,j]))
                elif grid[i][j] == 1:
                    freshOranges.add(tuple([i,j]))
        
        if not len(freshOranges):
            return 0
        
        count = 0
        
        while len(rottenOranges):
            curLen = len(rottenOranges)
            
            for _ in range(curLen):
                row,col = rottenOranges.popleft()
                
                left = tuple([row-1,col])
                if row > 0 and left in freshOranges:
                    freshOranges.remove(left)
                    rottenOranges.append(left)
                right = tuple([row+1,col])
                if row < m-1 and right in freshOranges:
                    freshOranges.remove(right)
                    rottenOranges.append(right)
                top = tuple([row,col-1])
                if col > 0 and top in freshOranges:
                    freshOranges.remove(top)
                    rottenOranges.append(top)
                bottom = tuple([row,col+1])
                if col < n-1 and bottom in freshOranges:
                    freshOranges.remove(bottom)
                    rottenOranges.append(bottom)
            count += 1
        
        return count-1 if not len(freshOranges) else -1
                