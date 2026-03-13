from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            inverse = target - num
            if inverse in seen:
                return [seen[inverse], i]
            seen[num] = i

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
