package main

import (
	"fmt"
	"math"
	"regexp"
	"strconv"

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
		carta:  map[coord]region{},
		depth:  depth,
		target: target,
	}
	for y := 0; y <= target.Y+moveBeyond; y++ {
		for x := 0; x <= target.X+moveBeyond; x++ {
			carta.newRegion(x, y)
		}
	}
	// carta.printCave()
	return carta.FindQuickestWay(savior{
		currentItem:  torch,
		currentCoord: coord{X: 0, Y: 0},
		timeTaken:    0})
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

var moveBeyond = 200

func (c *coord) add(other coord) coord {
	return coord{X: c.X + other.X, Y: c.Y + other.Y}
}

var directions = []coord{
	coord{X: -1, Y: 0},
	coord{X: 0, Y: -1},
	coord{X: 1, Y: 0},
	coord{X: 0, Y: 1},
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
	for y := 0; y <= c.target.Y+moveBeyond; y++ {
		line := ""
		for x := 0; x <= c.target.X+moveBeyond; x++ {
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

const (
	neither = iota
	climbingGear
	torch
)

func strItemName(item int) string {
	switch item {
	case neither:
		return "neither item"
	case climbingGear:
		return "climbing gear"
	case torch:
		return "torch"
	}
	return ""
}

func strRegionType(region int) string {
	switch region {
	case typeNarrow:
		return "narrow"
	case typeRocky:
		return "rocky"
	case typeWet:
		return "wet"
	}
	return ""
}

type savior struct {
	currentItem  int
	currentCoord coord
	timeTaken    int
}

func (s *savior) sameState(other savior) bool {
	return s.currentItem == other.currentItem && s.currentCoord == other.currentCoord
}

var allowedTools = map[int]map[int]bool{
	typeRocky:  map[int]bool{climbingGear: true, torch: true},
	typeWet:    map[int]bool{climbingGear: true, neither: true},
	typeNarrow: map[int]bool{torch: true, neither: true},
}

func (s *savior) newState(nextCoord coord, c *cartograph) []savior {
	nextMoves := []savior{}

	currentRegionType := c.carta[s.currentCoord].regionType
	nextRegionType := c.carta[nextCoord].regionType

	for item := range allowedTools[currentRegionType] {
		if item != s.currentItem {
			// fmt.Prinln("I can change to this item", item)
			nextMoves = append(nextMoves, savior{
				currentItem:  item,
				currentCoord: s.currentCoord,
				timeTaken:    s.timeTaken + 7,
			})
		}
		if item == s.currentItem && allowedTools[nextRegionType][item] {
			// fmt.Printf("    %s in %s region is ok I can move there with my current equipment.\r\n", strItemName(item), strRegionType(currentRegionType))
			nextMoves = append(nextMoves, savior{
				currentItem:  s.currentItem,
				currentCoord: nextCoord,
				timeTaken:    s.timeTaken + 1,
			})
		}
	}

	return nextMoves
}

type visitedRegion struct {
	pos  coord
	item int
}

func (c *cartograph) FindQuickestWay(startPos savior) int {
	finalPos := savior{currentItem: torch, currentCoord: c.target}
	minimalReachTime := int(math.MaxUint64 >> 1)

	visited := map[visitedRegion]int{}

	queue := []savior{startPos}
	for len(queue) > 0 {
		currentPos := queue[0]
		queue = queue[1:]
		// fmt.Printf("@%d - %v (%s) w/%s (#%d)\r\n",
		// 	currentPos.timeTaken,
		// 	currentPos.currentCoord,
		// 	strRegionType(c.carta[currentPos.currentCoord].regionType),
		// 	strItemName(currentPos.currentItem),
		// 	len(queue),
		// )
		regionInfo := visitedRegion{pos: currentPos.currentCoord, item: currentPos.currentItem}
		if val, ok := visited[regionInfo]; ok && val <= currentPos.timeTaken {
			// fmt.Println("  already visited this region with this equipment")
			continue
		} else {
			visited[regionInfo] = currentPos.timeTaken
		}

		//reached the end
		if finalPos.sameState(currentPos) {
			// fmt.Printf("target reached with time %d", currentPos.timeTaken)
			if currentPos.timeTaken < minimalReachTime {
				// it has reached the end in a better time than the others
				// fmt.Printf("  which is faster than %d\r\n", minimalReachTime)
				minimalReachTime = currentPos.timeTaken
			}
			// fmt.Printf("\r\n")
			continue
		}
		if currentPos.timeTaken > minimalReachTime {
			// fmt.Printf("  this way (%d) is slower than %d \r\n", currentPos.timeTaken, minimalReachTime)
			// there is no chance it will be faster
			continue
		}

		// move forward or change gear
		for _, dir := range directions {
			nextCoord := currentPos.currentCoord.add(dir)
			if _, ok := c.carta[nextCoord]; ok {
				// fmt.Printf("  try %v next\r\n", nextCoord)
				queue = append(queue, currentPos.newState(nextCoord, c)...)
			}

		}
	}

	return minimalReachTime
}
