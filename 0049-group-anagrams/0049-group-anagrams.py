class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupsDict = collections.defaultdict(list)
        
        for s in strs:
            cur = [0]*26
            for c in s:
                cur[ord(c)-97] += 1
            groupsDict[tuple(cur)].append(s)
        
        return groupsDict.values()