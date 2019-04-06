package main

import (
	"fmt"
	"math"
	"regexp"
	"strconv"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("10_2")
	result := GetSeconds(data)
	fmt.Println(result)
}

// GetSeconds gets text that is written in the ground
func GetSeconds(data []string) int {
	points := parseData(data)
	bounds := boundaries{math.MaxInt64 / 4, math.MinInt64 / 4, math.MaxInt64 / 4, math.MinInt64 / 4}
	seconds := 0
	didGrow := false
	for !didGrow {
		points, bounds, didGrow = simulate(points, bounds)
		seconds++
	}
	return seconds - 1
}

func parseData(data []string) []point {
	regex := *regexp.MustCompile(`position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>`)
	points := make([]point, len(data))
	for i, line := range data {
		parsedData := regex.FindStringSubmatch(line)
		posX, _ := strconv.Atoi(parsedData[1])
		posY, _ := strconv.Atoi(parsedData[2])
		velX, _ := strconv.Atoi(parsedData[3])
		velY, _ := strconv.Atoi(parsedData[4])
		points[i] = point{posX, posY, velX, velY}
	}
	return points
}

func simulate(points []point, prevBoundaries boundaries) ([]point, boundaries, bool) {
	startHeight := int(math.Abs(float64(prevBoundaries.maxY-prevBoundaries.minY))) + 1
	startWidth := int(math.Abs(float64(prevBoundaries.maxX-prevBoundaries.minX))) + 1
	newBoundaries := boundaries{math.MaxInt64, math.MinInt64, math.MaxInt64, math.MinInt64}
	newPoints := make([]point, len(points))
	for i, pt := range points {
		pt.posX += pt.velX
		pt.posY += pt.velY
		if pt.posX < newBoundaries.minX {
			newBoundaries.minX = pt.posX
		} else if pt.posX > newBoundaries.maxX {
			newBoundaries.maxX = pt.posX
		}
		if pt.posY < newBoundaries.minY {
			newBoundaries.minY = pt.posY
		} else if pt.posY > newBoundaries.maxY {
			newBoundaries.maxY = pt.posY
		}
		newPoints[i] = pt
	}
	endHeight := int(math.Abs(float64(newBoundaries.maxY-newBoundaries.minY))) + 1
	endWidth := int(math.Abs(float64(newBoundaries.maxX-newBoundaries.minX))) + 1
	didGrow := endWidth-startWidth > 0 || endHeight-startHeight > 0
	if didGrow {
		return points, prevBoundaries, true
	}
	return newPoints, newBoundaries, false
}

type point struct {
	posX int
	posY int
	velX int
	velY int
}

type boundaries struct {
	minX int
	maxX int
	minY int
	maxY int
}
