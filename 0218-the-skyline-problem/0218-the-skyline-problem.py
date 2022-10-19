class Solution:
    def merge(self,buildings,s,e):
        res = deque()
        if s > e:
            return res
        if s == e:
            res.append([buildings[s][0],buildings[s][2]])
            res.append([buildings[s][1],0])
            return res
        m = s + (e-s)//2
        left = self.merge(buildings,s,m)
        right = self.merge(buildings,m+1,e)
        leftH,rightH = 0, 0
        while len(left) or len(right):
            x1 = left[0][0] if len(left) else sys.maxsize
            x2 = right[0][0] if len(right) else sys.maxsize
            x = 0
            if x1 < x2:
                temp = left.popleft()
                x = temp[0]
                leftH = temp[1]
            elif x1 > x2:
                temp = right.popleft()
                x = temp[0]
                rightH = temp[1];
            else:
                temp = left.popleft()
                x = temp[0]
                leftH = temp[1]
                rightH = right.popleft()[1]
            
            h = max(leftH, rightH)
            if len(res) == 0 or h != res[-1][1]:
                res.append([x, h])
        return res
        
            
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        return list(self.merge(buildings,0,len(buildings)-1))
        