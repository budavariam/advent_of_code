package main

import (
	"fmt"
	"strconv"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("01_1")
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
