package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	input := utils.LoadInput("20_2")
	result := RegularMap(input[0])
	fmt.Println(result)
}

// RegularMap finds the number of shortest reachable distant rooms that is at least 1000 rooms away. Assuming that the rooms are first reached with the shortest path.
func RegularMap(input string) int {
	directions := map[rune]coord{
		'N': newCoord(-1, 0),
		'E': newCoord(0, 1),
		'S': newCoord(1, 0),
		'W': newCoord(0, -1),
	}
	distances := distanceMap{}
	level := []coord{}
	location := coord{}
	previousLocation := location
	for _, nextInputChar := range input {
		stackTop := len(level) - 1
		previousLocation = location
		switch nextInputChar {
		case '^':
		case '$':
		case '(':
			level = append(level, location)
		case ')':
			location = level[stackTop]
			level = level[:stackTop]
		case '|':
			location = level[stackTop]
		default:
			location = location.add(directions[nextInputChar])
			distances[location] = min(distances[previousLocation]+1, distances.get(location))
		}
	}

	countShortestPaths := 0
	for _, distance := range distances {
		if distance >= 1000 {
			countShortestPaths++
		}
	}
	return countShortestPaths
}
