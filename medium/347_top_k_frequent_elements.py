from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        result = []
        for f in range(len(freq) -1, 0, -1):
            for i in freq[f]:
                result.append(i)
                if len(result) == k:
                    return result

if __name__ == '__main__':

    sol = Solution()
    result = sol.topKFrequent([1, 2, 3, 1, 5, 5, 9], 2)
    print(result)
