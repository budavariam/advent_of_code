package main

import (
	"fmt"
)

type cartaRegion struct {
	erosionLevel  int
	geologicIndex int
	regionType    regionType
}

type cartograph struct {
	carta         map[coord]cartaRegion
	depth         int
	target        coord
	maxMoveBeyond int
}

func (c *cartograph) init() {
	for y := 0; y <= c.target.Y+c.maxMoveBeyond; y++ {
		for x := 0; x <= c.target.X+c.maxMoveBeyond; x++ {
			c.newRegion(x, y)
		}
	}
}

func (c *cartograph) newRegion(x, y int) {
	newData := cartaRegion{}
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
		riskLevelSum += int(region.regionType)
	}
	return riskLevelSum
}

func (c *cartograph) print() {
	for y := 0; y <= c.target.Y+c.maxMoveBeyond; y++ {
		line := ""
		for x := 0; x <= c.target.X+c.maxMoveBeyond; x++ {
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
