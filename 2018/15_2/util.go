package main

import "fmt"

// gets the absolute value for int values
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// printMap adds visualization for the current state, useful for for debug purposes
func printMap(data []string, units unitList) {
	result := make([]string, len(data))
	for y, line := range data {
		newLine := ""
		for _, char := range line {
			if char == '#' {
				newLine += "#"
			} else {
				newLine += "."
			}
		}
		result[y] = newLine
	}
	for _, u := range units {
		specChar := "E"
		if u.spec == goblin {
			specChar = "G"
		}
		result[u.pos.y] = result[u.pos.y][:u.pos.x] + specChar + result[u.pos.y][u.pos.x+1:]
	}
	for _, line := range result {
		fmt.Println(line)
	}
	fmt.Println("***")
}
