class Solution:
    def myPowHelper(self,x,n,c):
        if n in c:
            return c[n]
        nby2 = int(n/2)
        if int(math.fmod(n,2)):
            c[n] = self.myPowHelper(x,nby2,c)
            c[n] *= self.myPowHelper(x,nby2+1,c) if nby2 > 0 else self.myPowHelper(x,nby2-1,c)
            return c[n]
        c[n] = self.myPowHelper(x,nby2,c)**2
        return c[n]
    def myPow(self, x: float, n: int) -> float:
        if not x:
            return x
        c = collections.defaultdict(float)
        c[0] = 1
        c[1] = x
        c[-1] = 1/x
        return self.myPowHelper(x,n,c)