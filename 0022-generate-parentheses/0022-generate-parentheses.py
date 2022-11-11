class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set(["()"])
        
        n -= 1
        
        while n:
            tempres = set()
            
            for comb in res:
                tempres.add("()"+comb)
                for i in range(1,len(comb)):
                    newstr = comb[:i] + "()" + comb[i:]
                    tempres.add(newstr)
                tempres.add(comb+"()")
            res = set(tempres)
                
            n -= 1
        
        return res