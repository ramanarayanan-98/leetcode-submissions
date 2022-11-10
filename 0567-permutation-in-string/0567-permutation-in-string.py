class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1),len(s2)
        
        if m > n:
            return False
        
        s1chars = [0 for _ in range(26)]
        for ch in s1:
            s1chars[ord(ch)-97] += 1
            
        for i in range(m):
            s1chars[ord(s2[i])-97] -= 1
        
        if all([val <= 0 for val in s1chars]):
            return True
        
        for i in range(m,n):
            s1chars[ord(s2[i])-97] -= 1
            s1chars[ord(s2[i-m])-97] += 1
            
            if all([val <= 0 for val in s1chars]):
                return True
        
        return False