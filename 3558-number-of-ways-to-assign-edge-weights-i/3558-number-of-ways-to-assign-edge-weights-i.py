class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        queue = collections.deque([(1, 0)])
        visited = {1}
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
                    
        if max_depth == 0:
            return 0
            
        result = 1
        for i in range(max_depth - 1):
            result = (result * 2) % MOD
            
        return result