class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n <= 1:
            return 0
            
        value = {}
        for i, val in enumerate(arr):
            if val not in value:
                value[val] = []
            value[val].append(i)
            
        queue = deque([(0, 0)])
        visited = {0}
        
        while queue:
            curr_idx, steps = queue.popleft()
            
            if curr_idx == n - 1:
                return steps
                
            curr_val = arr[curr_idx]
            if curr_val in value:
                for next_idx in value[curr_val]:
                    if next_idx not in visited:
                        visited.add(next_idx)
                        queue.append((next_idx, steps + 1))
                del value[curr_val]
                
            if curr_idx + 1 < n and (curr_idx + 1) not in visited:
                visited.add(curr_idx + 1)
                queue.append((curr_idx + 1, steps + 1))
                
            if curr_idx - 1 >= 0 and (curr_idx - 1) not in visited:
                visited.add(curr_idx - 1)
                queue.append((curr_idx - 1, steps + 1))
                
        return 0