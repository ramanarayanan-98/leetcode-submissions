class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        curset = set()
        start,end = 0,0
        
        for end in range(0,len(s)):
            if s[end] not in curset:
                curset.add(s[end])
                maxLen = max(maxLen,len(curset))
                continue
            while start < end and s[end] in curset:
                curset.remove(s[start])
                start += 1
            curset.add(s[end])
        
        return maxLen
            