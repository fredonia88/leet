package main

import (
    "fmt"
)

func plusOne(digits []int) []int {
    for x := len(digits) - 1; x >= 0; x-- {
        if digits[x] == 9 {
            digits[x] = 0
        } else {
            digits[x] += 1
            return digits
        }
    }
    
    return append([]int{1}, digits...)

}

func main() {
	result := plusOne([]int{1,2,3})
	fmt.Println(result)
}