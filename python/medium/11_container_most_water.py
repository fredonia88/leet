class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            water = min(height[right], height[left]) * width
            max_water = max(max_water, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
    
if __name__ == '__main__':
    test = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    result = sol.maxArea(test)
    print(result)