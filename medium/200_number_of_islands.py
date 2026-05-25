from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        grid_len, row_len = len(grid) - 1, len(grid[0]) - 1
        
        def sink_island(grid, row, col):
            if row < 0 or row > grid_len:
                return
            elif col < 0 or col > row_len:
                return
            elif grid[row][col] != '1':
                return
            grid[row][col] = '2'
            sink_island(grid, row+1, col)
            sink_island(grid, row-1, col)
            sink_island(grid, row, col+1)
            sink_island(grid, row, col-1)

        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    sink_island(grid, r, c)
                    island_count += 1
        
        return island_count

if __name__ == '__main__':
    sol = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    result = sol.numIslands(grid)
    print(result)