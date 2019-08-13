package main

import (
	"fmt"
	"regexp"
	"strconv"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	input := utils.LoadInput("22_1")
	result := ModeMaze(input)
	fmt.Println(result)
}

// ModeMaze is the solution to the problem
func ModeMaze(input []string) int {
	depth, target := parseInput(input)
	carta := cartograph{
		carta:  map[coord]region{},
		depth:  depth,
		target: target,
	}
	for y := 0; y <= target.Y; y++ {
		for x := 0; x <= target.X; x++ {
			carta.newRegion(x, y)
		}
	}
	// carta.printCave()
	return carta.TotalRiskLevel()
}

func parseInput(data []string) (int, coord) {
	regexDepth := *regexp.MustCompile(`\w+: (\d+)`)

	rawDepth := regexDepth.FindStringSubmatch(data[0])
	depth, _ := strconv.Atoi(rawDepth[1])
	regexCoord := *regexp.MustCompile(`\w+: (\d+),(\d+)`)
	rawTarget := regexCoord.FindStringSubmatch(data[1])
	targetX, _ := strconv.Atoi(rawTarget[1])
	targetY, _ := strconv.Atoi(rawTarget[2])
	target := coord{X: targetX, Y: targetY}

	return depth, target
}

const (
	typeRocky = iota
	typeWet
	typeNarrow
)

type coord struct {
	X int
	Y int
}

type region struct {
	erosionLevel  int
	geologicIndex int
	regionType    int
}

func (c *cartograph) newRegion(x, y int) {
	newData := region{}
	if x == 0 && y == 0 {
		newData.geologicIndex = 0
	} else if x == c.target.X && y == c.target.Y {
		newData.geologicIndex = 0
	} else if y == 0 {
		newData.geologicIndex = x * 16807
	} else if x == 0 {
		newData.geologicIndex = y * 48271
	} else {
		newData.geologicIndex = c.carta[coord{X: x - 1, Y: y}].erosionLevel * c.carta[coord{X: x, Y: y - 1}].erosionLevel
	}
	newData.erosionLevel = (newData.geologicIndex + c.depth) % 20183
	switch newData.erosionLevel % 3 {
	case 0:
		newData.regionType = typeRocky
	case 1:
		newData.regionType = typeWet
	case 2:
		newData.regionType = typeNarrow
	}
	c.carta[coord{X: x, Y: y}] = newData
}

func (c *cartograph) TotalRiskLevel() int {
	riskLevelSum := 0
	for _, region := range c.carta {
		riskLevelSum += region.regionType
	}
	return riskLevelSum
}

func (c *cartograph) printCave() {
	for y := 0; y <= c.target.Y; y++ {
		line := ""
		for x := 0; x <= c.target.X; x++ {
			regionMarker := ""
			switch c.carta[coord{X: x, Y: y}].regionType {
			case 0:
				regionMarker = "."
			case 1:
				regionMarker = "="
			case 2:
				regionMarker = "|"
			}
			line += regionMarker
		}
		fmt.Println(line)
	}
}

type cartograph struct {
	carta  map[coord]region
	depth  int
	target coord
}
