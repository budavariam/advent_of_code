package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("06_2")
	result := NearManyCoordinates(data, 10000)
	fmt.Println(result)
}

// NearManyCoordinates counts the largest area that is within the threshold distance of other coordinates
func NearManyCoordinates(input []string, threshold int) int {
	coords, boundaries := normalizeCoords(input)
	sum := 0
	for y := 0; y < boundaries.maxy; y++ {
		for x := 0; x < boundaries.maxx; x++ {
			summary := 0
			for _, coord := range coords {
				summary += int(math.Abs(float64(x-coord.x)) + math.Abs(float64(y-coord.y)))
				if summary > threshold {
					break
				}
			}
			if summary < threshold {
				sum++
			}
		}
	}
	return sum
}

type point struct {
	x  int
	y  int
	id int
}

// bounds defines the dimensions of the matrix, lower inclusive, upper exclusive
type bounds struct {
	minx int
	miny int
	maxx int
	maxy int
}

// normalizeCoords converts the input string to coords, and translates them to (0,0)
func normalizeCoords(coords []string) ([]point, bounds) {
	result := make([]point, len(coords))
	minX, minY, maxX, maxY := math.MaxInt64, math.MaxInt64, 0, 0
	for index, currentPoint := range coords {
		splitted := strings.Split(currentPoint, ", ")
		x, _ := strconv.Atoi(splitted[0])
		y, _ := strconv.Atoi(splitted[1])
		if x < minX {
			minX = x
		}
		if x > maxX {
			maxX = x
		}
		if y < minY {
			minY = y
		}
		if y > maxY {
			maxY = y
		}
		result[index].x = x
		result[index].y = y
		result[index].id = index
	}
	// Translate the coords to start at (0, 0)
	for index, value := range result {
		value.x -= minX
		value.y -= minY
		result[index] = value
	}
	return result, bounds{minx: 0, miny: 0, maxx: maxX - minX + 1, maxy: maxY - minX + 1}
}
