package main

import (
	"fmt"
	"strings"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	input := utils.LoadInput("18_1")
	result := SimulateLumberChange(input)
	fmt.Println(result)
}

// SimulateLumberChange ticks one minute in tis changing world
func SimulateLumberChange(input []string) int {
	carta := parseInput(input)
	for i := 0; i < 10; i++ {
		carta = carta.Simulate()
		//carta.printMap()
	}
	return carta.GetLumberYardCount() * carta.GetWoodenAcreCount()
}

type carta [][]kind
type kind int

const (
	openGround = iota
	tree
	lumberYard

	openGroundMarker = "."
	treeMarker       = "|"
	lumberYardMarker = "#"
)

var directions = [][2]int{
	[2]int{-1, -1},
	[2]int{-1, 0},
	[2]int{-1, 1},
	[2]int{0, -1},
	[2]int{0, 1},
	[2]int{1, -1},
	[2]int{1, 0},
	[2]int{1, 1},
}

func parseInput(input []string) carta {
	carta := make(carta, len(input))
	for y, rawLine := range input {
		line := strings.Split(rawLine, "")
		cartaLine := make([]kind, len(line))
		for x, tile := range line {
			var spot int
			switch tile {
			case openGroundMarker:
				spot = openGround
			case treeMarker:
				spot = tree
			case lumberYardMarker:
				spot = lumberYard
			}
			cartaLine[x] = kind(spot)
		}
		carta[y] = cartaLine
	}
	return carta
}

func (c carta) countAcres(k kind) int {
	counter := 0
	for _, line := range c {
		for _, acre := range line {
			if acre == k {
				counter++
			}
		}
	}
	return counter
}

func (c carta) GetWoodenAcreCount() int {
	return c.countAcres(tree)
}

func (c carta) GetLumberYardCount() int {
	return c.countAcres(lumberYard)
}

// Simulate calculates the state of the next minute
func (c carta) Simulate() carta {
	result := make(carta, len(c))
	for y, line := range c {
		cartaLine := make([]kind, len(line))
		for x, acre := range line {
			cartaLine[x] = c.nextState(y, x, acre)
		}
		result[y] = cartaLine
	}
	return result
}

// nextState gets the new kind of that spot according to the previous state
//
// An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.
// An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. Otherwise, nothing happens.
// An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
func (c carta) nextState(y, x int, acre kind) kind {
	adjacentFieldsKindCounter := [3]kind{}
	maxHeight := len(c)
	maxWidth := len(c[0])
	for _, dir := range directions {
		newY, newX := dir[0]+y, dir[1]+x
		if newY >= 0 && newY < maxHeight && newX >= 0 && newX < maxWidth {
			adjacentFieldsKindCounter[c[newY][newX]]++
		}
	}
	var result kind
	switch acre {
	case openGround:
		if adjacentFieldsKindCounter[tree] >= 3 {
			result = tree
		} else {
			result = openGround
		}
	case tree:
		if adjacentFieldsKindCounter[lumberYard] >= 3 {
			result = lumberYard
		} else {
			result = tree
		}
	case lumberYard:
		if adjacentFieldsKindCounter[lumberYard] >= 1 && adjacentFieldsKindCounter[tree] >= 1 {
			result = lumberYard
		} else {
			result = openGround
		}
	}
	return result
}

// printMap gives debug info for development
func (c carta) printMap() {
	for _, line := range c {
		fmt.Println(line)
	}
	fmt.Println("-----")
}
