from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1,n+1):
            val = ""
            if i % 3 == 0:
                val += "Fizz"
            if i % 5 == 0:
                val += "Buzz"
            if not val:
                val += str(i)
            answer.append(val)

        return answer

if __name__ == '__main__':
    sol = Solution()
    result = sol.fizzBuzz(5)
    print(result)
