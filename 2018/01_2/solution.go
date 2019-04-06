package main

import (
	"fmt"
	"strconv"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("01_2")
	result := ReachTwiceFirst(data)
	fmt.Println(result)
}

// ReachTwiceFirst gets the first number that is reached twice
func ReachTwiceFirst(data []string) int {
	result := 0
	frequencySet := make(map[int]bool)
OuterLoop:
	for {
		for _, data := range data {
			d, _ := strconv.Atoi(data)
			if frequencySet[result] {
				break OuterLoop
			} else {
				frequencySet[result] = true
				result += d
			}
		}
	}
	return result
}
