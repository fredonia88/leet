class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) == 1 or numRows == 1:
            return s

        idx, d = 0, 1
        rows = [[] for row in range(numRows)]

        for c in s:
            rows[idx].append(c)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        
        result = ''
        for i in range(len(rows)):
            result += rows[i]
            
        return result

if __name__ == '__main__':
    test_s = 'PAYPALISHIRING'
    num_rows = 3

    sol = Solution()
    res = sol.convert(test_s, num_rows)
    print(res)