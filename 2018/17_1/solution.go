package main

import (
	"fmt"
	"math"
	"regexp"
	"strconv"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("17_1")
	result := ReservoirResearch(data)
	fmt.Println(result)
}

const (
	typeSand = iota
	typeSource
	typeFlow
	typeStillwater
	typeClay
)

const (
	dirDown = iota
	dirLeft
	dirRight
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// coord [x,y]
type coord [2]int
type carta map[coord]int

type cartography struct {
	carta carta
	maxX  int
	maxY  int
	minX  int
	minY  int
}

func newCartography(sourceLocation coord) cartography {
	sourceX, sourceY := sourceLocation[0], sourceLocation[1]
	c := cartography{carta: carta{coord{sourceX, sourceY}: typeSource}}
	c.minX, c.maxX, c.minY, c.maxY = sourceX, sourceX, math.MaxInt64, sourceY
	return c
}

func (c *cartography) drawLine(startX, endX, startY, endY, elementType int) {
	if startX > endX || startY > endY {
		panic(fmt.Sprintf("Bad assumption (%d-%d, %d-%d)", startX, endX, startY, endY))
	}

	for x := startX; x <= endX; x++ {
		for y := startY; y <= endY; y++ {
			coordinate := coord{x, y}
			if c.carta[coordinate] != typeStillwater {
				c.carta[coordinate] = elementType
			}
		}
	}

	if elementType == typeClay {
		// set boundaries only in init state
		c.maxX = max(c.maxX, endX)
		c.maxY = max(c.maxY, endY)
		c.minX = min(c.minX, startX)
		c.minY = min(c.minY, startY)
	}
}

func (c *cartography) printMap() {
	for y := c.minY - 2; y <= c.maxY+2; y++ {
		for x := c.minX - 2; x <= c.maxX+2; x++ {
			mark := " "
			if val, ok := c.carta[coord{x, y}]; ok {
				switch val {
				case typeClay:
					mark = "#"
				case typeFlow:
					mark = "|"
				case typeSource:
					mark = "+"
				case typeStillwater:
					mark = "~"
				default:
					mark = " "
				}
			}
			fmt.Printf(mark)
		}
		fmt.Printf("\r\n")
	}
}

func (c *cartography) simulateFlow(source coord) {
	c.moveWater(source, dirDown)
}

func (c *cartography) moveToTheSide(prev coord, direction int) (bool, int) {
	var nextX int
	if direction == dirLeft {
		nextX = prev[0] - 1
	} else {
		nextX = prev[0] + 1
	}

	curr := coord{nextX, prev[1]}
	if val, ok := c.carta[curr]; ok && (val == typeClay || val == typeStillwater) {
		return true, prev[0]
	}
	under := coord{curr[0], curr[1] + 1}
	if val, ok := c.carta[under]; !ok || (val == typeFlow) {
		// if it can go down, change direction
		c.simulateFlow(curr)
		return false, curr[0]
	}
	return c.moveWater(curr, direction)
}

func (c *cartography) moveWater(prev coord, direction int) (bool, int) {
	switch direction {
	case dirDown:
		curr := coord{prev[0], prev[1] + 1}
		if curr[1] > c.maxY {
			return false, -1
		}
		if val, ok := c.carta[curr]; ok {
			if val == typeClay || val == typeStillwater {
				leftWall, startLine := c.moveWater(prev, dirLeft)
				rightWall, endLine := c.moveWater(prev, dirRight)
				elementType := typeFlow
				if rightWall && leftWall {
					elementType = typeStillwater
				}
				c.drawLine(startLine, endLine, prev[1], prev[1], elementType)
				if leftWall && rightWall {
					return c.moveWater(coord{prev[0], prev[1] - 1}, dirDown) // if both sides hit a wall then continue upwards
				}
			}
			return false, -1
		}
		c.carta[curr] = typeFlow
		return c.moveWater(curr, dirDown)
	case dirLeft:
		return c.moveToTheSide(prev, dirLeft)
	case dirRight:
		return c.moveToTheSide(prev, dirRight)
	default:
		return false, -1 // should not be here
	}
}

func (c *cartography) countWaterInVisibleRange() int {
	result := 0
	for place, v := range c.carta {
		if place[1] >= c.minY && place[1] <= c.maxY && (v == typeFlow || v == typeStillwater) {
			result++
		}
	}
	return result
}

// ReservoirResearch is the solution to the problem
func ReservoirResearch(data []string) int {
	source := [2]int{500, 0}
	ground := parseMap(newCartography(source), data)
	ground.simulateFlow(source)
	result := ground.countWaterInVisibleRange()
	//ground.printMap()
	return result
}

func parseMap(ground cartography, raw []string) cartography {
	pattern := regexp.MustCompile(`([xy])=(\d+), [xy]=(\d+)..(\d+)`)
	for _, line := range raw {
		p := pattern.FindStringSubmatch(line)
		nr1, _ := strconv.Atoi(p[2])
		nr2, _ := strconv.Atoi(p[3])
		nr3, _ := strconv.Atoi(p[4])
		if p[1] == "x" {
			ground.drawLine(nr1, nr1, nr2, nr3, typeClay)
		} else {
			ground.drawLine(nr2, nr3, nr1, nr1, typeClay)
		}
	}
	return ground
}
