class Solution:
    def differsByOne(self,s1,s2):
        if len(s1) ^ len(s2):
            return False
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        
        return count == 1
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)     
        if endWord not in wordset:
            return 0
        queue = deque()
        visited = set()
        beginwordlist = [x for x in beginWord]
        visited.add(beginWord)
        queue.append(beginwordlist)
        count = 1
        
        while len(queue):
            length = len(queue)
            
            for _ in range(length):
                curnode = queue.popleft()
                
                if "".join(curnode) == endWord:
                    return count
                
                for i in range(len(curnode)):
                    for c in range(97,97+26):
                        temp = curnode[i]
                        curnode[i] = chr(c)
                        string = "".join(curnode)
                        
                        if string in wordset and string not in visited:
                            queue.append(list(curnode)) 
                            visited.add(string)
                        curnode[i] = temp
            
            count += 1
        return 0
                
                
        
                    