package main

import (
	"advent_of_code/2018/utils"
	"fmt"
	"regexp"
	"strconv"
)

func main() {
	data := utils.LoadInput("03_1/input.txt")
	result := CalculateOverlappingFabric(data, 1000, 1000)
	fmt.Println(result)
}

// CalculateOverlappingFabric calculates how many inches are overlapping in the fabric
func CalculateOverlappingFabric(data []string, width int, height int) int {
	fabricMatrix := InitMatrix(width, height)
	overlaps := map[string]bool{}
	for _, line := range data {
		regex := *regexp.MustCompile(`#\d+ @ (\d+),(\d+): (\d+)x(\d+)`)
		parsedData := regex.FindAllStringSubmatch(line, -1)
		FillMatrix(fabricMatrix, parsedData, overlaps)
	}
	return len(overlaps)
}

// InitMatrix initializes a 2d slice with false values.
func InitMatrix(width int, height int) [][]bool {
	matrix := make([][]bool, height)
	for y := 0; y < height; y++ {
		matrix[y] = make([]bool, width)
		for x := 0; x < width; x++ {
			matrix[y][x] = false
		}
	}
	return matrix
}

// FillMatrix marks the fabric of what to cut, and sets the overlaps
func FillMatrix(matrix [][]bool, res [][]string, overlaps map[string]bool) {
	leftm, _ := strconv.Atoi(res[0][1])
	topm, _ := strconv.Atoi(res[0][2])
	width, _ := strconv.Atoi(res[0][3])
	height, _ := strconv.Atoi(res[0][4])
	for y := topm; y < topm+height; y++ {
		for x := leftm; x < leftm+width; x++ {
			if matrix[y][x] {
				overlaps[fmt.Sprintf("%d-%d", y, x)] = true
			}
			matrix[y][x] = true
		}
	}
}
