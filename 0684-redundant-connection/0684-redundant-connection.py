class Solution:
    def dfs(self,source,target,seen,graph)->bool:
        if source in seen:
            return False
        if source == target:
            return True
        seen.add(source)
        return any(self.dfs(nei,target,seen,graph) for nei in graph[source])
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u,v in edges:
            seen = set()
            if u in graph and v in graph and self.dfs(u,v,seen,graph):
                return [u,v]
            graph[u].append(v)
            graph[v].append(u)
        