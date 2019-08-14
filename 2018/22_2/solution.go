package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	input := utils.LoadInput("22_2")
	result := ModeMaze(input)
	fmt.Println(result)
}

// ModeMaze is the solution to the problem
func ModeMaze(input []string) int {
	depth, target := parseInput(input)
	carta := cartograph{
		carta:         map[coord]cartaRegion{},
		depth:         depth,
		target:        target,
		maxMoveBeyond: 200,
	}

	carta.init()
	// carta.print()

	startPos := savior{
		currentItem:  torch,
		currentCoord: coord{X: 0, Y: 0},
		timeTaken:    0,
	}
	return startPos.FindQuickestWay(&carta)
}
