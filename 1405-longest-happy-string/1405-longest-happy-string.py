class Solution:
    def getSameLastTwo(self,res):
        return res[-1] if len(res) >= 2 and res[-1] == res[-2] else ""
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        for i in range(a+b+c):
            if a == max(a,b,c) and self.getSameLastTwo(res) != "a" or (self.getSameLastTwo(res) in ["b","c"] and a>0):
                res += "a"
                a -= 1
            elif b == max(a,b,c) and self.getSameLastTwo(res) != "b" or (self.getSameLastTwo(res) in ["a","c"] and b>0):
                res += "b"
                b -= 1
            elif c == max(a,b,c) and self.getSameLastTwo(res) != "c" or (self.getSameLastTwo(res) in ["b","a"] and c>0):
                res += "c"
                c -= 1
        return res