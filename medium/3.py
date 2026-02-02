import time


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        s_len = len(s)
        for n, c in enumerate(s):
            if s_len - n + 1 < max_len:
                break
            new_s = ''
            for c in s[n:]:
                if c not in new_s:
                    new_s += c
                else:
                    break
                max_len = len(new_s) if len(new_s) > max_len else max_len
        return max_len


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        c_map = {}

        for i, c in enumerate(s):
            if c in c_map and c_map[c] >= left:
                left = c_map[c] + 1
            c_map[c] = i
            max_len = max(max_len, i + 1 - left)
        
        return max_len


if __name__ == '__main__':
    test_s = 'abcabcbb'

    sol1 = Solution1()
    t0 = time.perf_counter()
    res1 = sol1.lengthOfLongestSubstring(test_s)
    t1 = time.perf_counter()
    print('Solution1 result:', res1, 'time:', t1 - t0)

    sol2 = Solution2()
    t2 = time.perf_counter()
    res2 = sol2.lengthOfLongestSubstring(test_s)
    t3 = time.perf_counter()
    print('Solution2 result:', res2, 'time:', t3 - t2)
