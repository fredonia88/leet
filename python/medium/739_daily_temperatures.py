from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = (i - prev_index)
            stack.append(i)
        
        return result

if __name__ == '__main__':
    sol = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    result = sol.dailyTemperatures(temperatures)
    print(result)
