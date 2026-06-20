package main

import (
	"fmt"
)

type coor struct {
    r, c int
}

func findPath(row int, col int, grid [][]int, max_row int, max_col int, cache map[coor]int) int {

    row_col := coor{r: row, c: col}
    if sum, exists := cache[row_col]; exists {
        return sum
    }
    
    var result int
    switch {
    case row == max_row && col == max_col:
        result = grid[row][col]
    case row == max_row:
        result = grid[row][col] + findPath(row, col+1, grid, max_row, max_col, cache)
    case col == max_col:
        result = grid[row][col] + findPath(row+1, col, grid, max_row, max_col, cache)
    default:
        go_down := findPath(row+1, col, grid, max_row, max_col, cache)
        go_right := findPath(row, col+1, grid, max_row, max_col, cache)
        result = grid[row][col] + min(go_down, go_right)
    }

    cache[row_col] = result
    return result
}

func minPathSum(grid [][]int) int {
    max_row, max_col := len(grid) - 1, len(grid[0]) - 1
    cache := make(map[coor]int)

    return findPath(0, 0, grid, max_row, max_col, cache)
}

func main() {
	grid := [][]int{
		{1,3,1},
		{1,5,1},
		{4,2,1},
	}
	result := minPathSum(grid)
	fmt.Println(result)
}