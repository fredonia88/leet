class Solution:
    def myAtoi(self, s: str) -> int:
        reading = False
        i = ''
        sign = 1
        s = s.strip()
        for c in s:
            if not reading and c == '+':
                reading = True
                continue
            elif not reading and c == '-': 
                reading = True
                sign = -1
            elif not c.isdigit():
                break
            else:
                i += c
                reading = True
        i = int(i) * sign if len(i) > 0 else 0

        if i > 2**31-1:
            return 2**31-1
        elif i < -2**31:
            return -2**31
        else:
            return i

if __name__ == '__main__':
    x = '-12:'
    sol = Solution()
    result = sol.myAtoi(x)
    print(result)
