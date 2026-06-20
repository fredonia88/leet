from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        max_row, max_col = len(grid), len(grid[0])
        cache = {}
        
        def find_path(row: int, col: int) -> int:

            if (row, col) in cache:
                return cache[(row, col)]
            
            # base case
            if row == max_row - 1 and col == max_col - 1:
                return grid[row][col]
            
            # end of row, can only move down
            if row == max_row - 1:
                return grid[row][col] + find_path(row, col + 1)
            
            # end of col, can only move right
            if col == max_col - 1:
                return grid[row][col] + find_path(row + 1, col)
            
            # take the min of going down and going right
            go_down = find_path(row + 1, col)
            go_right = find_path(row, col + 1)

            result = grid[row][col] + min(go_down, go_right)
            cache[(row, col)] = result
            return result
        
        return find_path(0, 0)
    
if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    sol = Solution()
    result = sol.minPathSum(grid)
    print(result)