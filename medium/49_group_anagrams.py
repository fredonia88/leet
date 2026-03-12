from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for st in strs:
            key = ''.join(sorted(st))
            groups.setdefault(key, []).append(st)
        
        return list(groups.values())

if __name__ == '__main__':
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(strs))