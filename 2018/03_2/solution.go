package main

import (
	"fmt"
	"regexp"
	"strconv"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("03_2")
	result := CalculateNonOverlappingFabric(data, 1000, 1000)
	fmt.Println(result)
}

// CalculateNonOverlappingFabric calculates which fabric does not overlap
func CalculateNonOverlappingFabric(data []string, width int, height int) int {
	fabricMatrix := InitMatrix(width, height)
	overlaps := map[int]bool{}
	for _, line := range data {
		regex := *regexp.MustCompile(`#(\d+) @ (\d+),(\d+): (\d+)x(\d+)`)
		parsedData := regex.FindAllStringSubmatch(line, -1)
		FillMatrix(fabricMatrix, parsedData, overlaps)
	}
	nonoverlapping := FindNonOverlapping(overlaps)
	return nonoverlapping
}

// InitMatrix initializes a 2d slice with false values.
func InitMatrix(width int, height int) [][]int {
	matrix := make([][]int, height)
	for y := 0; y < height; y++ {
		matrix[y] = make([]int, width)
		for x := 0; x < width; x++ {
			matrix[y][x] = 0
		}
	}
	return matrix
}

// FillMatrix marks the fabric of what to cut, and sets the overlaps
func FillMatrix(matrix [][]int, res [][]string, overlaps map[int]bool) {
	index, _ := strconv.Atoi(res[0][1])
	leftm, _ := strconv.Atoi(res[0][2])
	topm, _ := strconv.Atoi(res[0][3])
	width, _ := strconv.Atoi(res[0][4])
	height, _ := strconv.Atoi(res[0][5])
	if !overlaps[index] {
		// Make sure that the current index is in the 'set'.
		overlaps[index] = false
	}
	for y := topm; y < topm+height; y++ {
		for x := leftm; x < leftm+width; x++ {
			if matrix[y][x] != 0 {
				// Mark the two overlapping fabrics in the overlaps set
				overlaps[matrix[y][x]] = true
				overlaps[index] = true
			}
			// Set which fabric lays in that place
			matrix[y][x] = index
		}
	}
}

// FindNonOverlapping returns the only one false value from the overlaps set
func FindNonOverlapping(overlaps map[int]bool) int {
	for index, isOverlapping := range overlaps {
		if !isOverlapping {
			return index
		}
	}
	return -1
}
