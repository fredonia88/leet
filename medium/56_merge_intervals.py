from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = result[-1][1]

            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])
        
        return result
    
if __name__ == '__main__':
    sol = Solution()
    result = sol.merge([[1,3],[2,6],[8,10],[15,18]])
    print(result)