class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) ^ len(t):
            return False
        
        charsarray = [0]*128
        
        for i in range(len(s)):
            charsarray[ord(s[i])] += 1
            charsarray[ord(t[i])] -= 1
        
        return all([not val for val in charsarray])