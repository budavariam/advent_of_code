package main

import (
	"fmt"
	"strings"
	"sync"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	input := utils.LoadInput("18_1")
	result := SimulateLumberChange(input)
	fmt.Println(result)
}

// SimulateLumberChange ticks one minute in tis changing world
func SimulateLumberChange(input []string) int {
	init := parseInput(input)
	lastState := init.SimulateNum(1000000000)
	resLumber, resWood := lastState.GetLumberYardCount(), lastState.GetWoodenAcreCount()
	return resLumber * resWood
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

var (
	maxHeight  = 0
	maxWidth   = 0
	cartaSize  = 0
	directions = [][2]int{
		[2]int{-1, -1},
		[2]int{-1, 0},
		[2]int{-1, 1},
		[2]int{0, -1},
		[2]int{0, 1},
		[2]int{1, -1},
		[2]int{1, 0},
		[2]int{1, 1},
	}
)

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
	maxHeight = len(carta)
	maxWidth = len(carta[0])
	cartaSize = maxHeight * maxWidth
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
func (c carta) simulate() carta {
	var waitgroup sync.WaitGroup
	waitgroup.Add(cartaSize)

	result := make(carta, len(c))
	for y, line := range c {
		cartaLine := make([]kind, len(line))
		for x, acre := range line {
			go func(cartaLine []kind, y, x int, acre kind) {
				cartaLine[x] = c.nextState(y, x, acre)
				waitgroup.Done()
			}(cartaLine, y, x, acre)
		}
		result[y] = cartaLine
	}
	waitgroup.Wait()
	return result
}

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
func (c carta) printMap(i int) {
	fmt.Println("#", i)
	for _, line := range c {
		printLine := ""
		for _, acre := range line {
			switch acre {
			case openGround:
				printLine += openGroundMarker
			case lumberYard:
				printLine += lumberYardMarker
			case tree:
				printLine += treeMarker
			}
		}
		fmt.Println(printLine)
	}
	fmt.Println("-----")
}

type periodic []carta

func getPeriodicity(init carta) (int, int, periodic) {
	prevState := init
	simulationNumber := 0
	p := make(periodic, 0)
	for {
		newState := prevState.simulate()
		for equalIndex, state := range p {
			if state.Equal(newState) {
				fmt.Printf("Periodicity found at index %d for #%d simulation\r\n", equalIndex, simulationNumber)
				return equalIndex, simulationNumber, p
			}
		}
		simulationNumber++
		prevState = newState
		p = append(p, newState)
		// newState.printMap(simulationNumber)
	}
}

// Simulate n minutes
func (c carta) SimulateNum(n int) carta {

	firstPeriodStart, firstPeriodEnd, periods := getPeriodicity(c)

	permutationLength := firstPeriodEnd - firstPeriodStart
	nth := (n - firstPeriodStart) % permutationLength
	offset := firstPeriodStart - 1

	return periods[offset+nth]
}

// Equal tells whether a and b contain the same elements.
func (c carta) Equal(other carta) bool {
	for y, line := range c {
		for x, acre := range line {
			if acre != other[y][x] {
				return false
			}
		}
	}
	return true
}
