package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

// ChronalClassification is the solution to the problem
func ChronalClassification(data []string) int {
	observations := parseObservations(data)
	result := 0
	for _, observation := range observations {
		howMany := calcPossibilities(observation)
		if howMany >= 3 {
			result++
		}
	}
	return result
}

func main() {
	data := utils.LoadInput("16_1")
	result := ChronalClassification(data)
	fmt.Println(result)
}
