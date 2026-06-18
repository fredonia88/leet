from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('-inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target - total) < abs(target - closest):
                    closest = total

                if closest == target:
                    return closest
                elif total < target: 
                    left += 1
                else:
                    right -= 1
        
        return closest
    
if __name__ == '__main__':
    sol = Solution()
    nums = [-1,2,1,-4]
    target = 1
    result = sol.threeSumClosest(nums, target)
    print(result)