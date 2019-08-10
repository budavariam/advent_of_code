package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	input := utils.LoadInput("20_1")
	result := RegularMap(input[0])
	fmt.Println(result)
}

// RegularMap finds the shortest reachable distance for the furthest room availabele. Assuming that the rooms are first reached with the shortest path.
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
	shortestPath := 0
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
			shortestPath = max(distances[location], shortestPath)
		}
	}
	return shortestPath
}
