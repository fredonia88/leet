import time

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        y = str(abs(x))[::-1]
        y = int(y) * sign
        if y.bit_length() >= 32:
            return 0
        else:
            return y
        
class SolutionFaster:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        y = 0
        while x:
            y = y * 10 + x % 10
            x //= 10
        y *= sign
        return y if -2**31 <= y <= 2**31 else 0

if __name__ == '__main__':
    text_x = 123

    sol = Solution()
    t0 = time.perf_counter()
    result = sol.reverse(text_x)
    t1 = time.perf_counter()
    print('Solution result:', result, 'time:', t1 - t0)

    sol = SolutionFaster()
    t0 = time.perf_counter()
    result = sol.reverse(text_x)
    t1 = time.perf_counter()
    print('Solution result:', result, 'time:', t1 - t0)