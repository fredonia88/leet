class Solution:
    def longestPalindrome(self, s: str) -> str:

        def len_pal(l, r): 
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r
        
        start = end = 0
        for i in range(len(s)):
            l, r = len_pal(i, i)
            if r - l > end - start:
                start, end = l, r

            l, r = len_pal(i, i+1)
            if r - l > end - start:
                start, end = l, r

        return s[start:end]
    
if __name__ == '__main__':
    test = 'babad'
    sol = Solution()
    pal = sol.longestPalindrome(test)
    print(pal)