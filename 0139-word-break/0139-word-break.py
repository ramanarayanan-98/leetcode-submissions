class Solution:
    def wordBreakHelper(self,s,wordset,curIdx,cache):
        if curIdx in cache:
            return cache[curIdx]
        
        for i in range(curIdx,len(s)):
            if s[curIdx:i+1] in wordset:
                if self.wordBreakHelper(s,wordset,i+1,cache):
                    cache[i+1] = True
                    return True
        cache[curIdx] = False
        return False
                    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        cache = collections.defaultdict(bool)
        cache[len(s)] = True
        return self.wordBreakHelper(s,wordset,0,cache)