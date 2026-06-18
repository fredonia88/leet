from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            
            state[node] = 1

            for n in graph[node]:
                if not dfs(n):
                    return False
            
            state[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

if __name__ == '__main__':
    sol = Solution()
    result = sol.canFinish(2, [[1,0],[0,1]])
    print(result)