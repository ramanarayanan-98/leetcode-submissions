class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target-p)/s for p,s in sorted(zip(position,speed))]
        res,maxt = 0,0
        
        for t in reversed(time):
            if t > maxt:
                res += 1
                maxt = t
        
        return res
        
        




        
        