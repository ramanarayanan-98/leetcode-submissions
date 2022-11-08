class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        totCount = 0
        for i in range(n):
            count = 1

            # odd
            offset = 1
            while i-offset >= 0 and i+offset < n and s[i-offset] == s[i+offset]:
                count += 1
                offset += 1

            # even
            offset = 1
            while i-offset >= 0 and i+offset-1 < n and s[i-offset] == s[i+offset-1]:
                count += 1
                offset += 1
            totCount += count

        return totCount
            
