from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []

        if len(nums) < 4:
            return results

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
               continue
            
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                   continue

                left, right = j + 1, len(nums) - 1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s > target:
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
                        left += 1

        return results

if __name__ == '__main__':
    sol = Solution()
    result = sol.fourSum([1,0,-1,0,-2,2], 0)
    print(result)