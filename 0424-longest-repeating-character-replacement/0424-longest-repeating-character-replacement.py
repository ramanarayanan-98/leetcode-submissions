class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start,end = 0,0
        n = len(s)
        maxcount = 0
        maxlength = 0
        charcount = [0 for _ in range(26)]
        
        while end < n:
            charcount[ord(s[end])-65] += 1
            maxcount = max(maxcount,charcount[ord(s[end])-65])
            
            if end-start+1-maxcount > k:
                charcount[ord(s[start])-65] -= 1
                start += 1
            
            maxlength = max(maxlength,end-start+1)
            end += 1
            
        return maxlength
            