class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        y = str(abs(x))[::-1]
        y = int(y) * sign
        if y.bit_length() >= 32:
            return 0
        else:
            return y

if __name__ == '__main__':
    text_x = 123

    sol = Solution()
    result = sol.reverse(text_x)
    print(result)