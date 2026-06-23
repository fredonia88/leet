from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        output = []

        def backtrack(index, current):

            if index == len(digits):
                output.append(current)
                return
            
            for letter in num_map[digits[index]]:
                backtrack(index + 1, current + letter)
        
        backtrack(0, '')
        return output
            
if __name__ == '__main__':
    sol = Solution()
    result = sol.letterCombinations("23")
    print(result)