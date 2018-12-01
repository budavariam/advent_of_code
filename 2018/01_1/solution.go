package main

import (
	"advent_of_code/2018/utils"
	"fmt"
	"strconv"
)

func main() {
	data := utils.LoadInput("01_1/input.txt")
	result := Sum(data)
	fmt.Println(result)
}

// Sum summarizes the frequencies
func Sum(data []string) int {
	result := 0
	for _, data := range data {
		d, _ := strconv.Atoi(data)
		result += d
	}
	return result
}
