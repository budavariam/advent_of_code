package main

import (
	"advent_of_code/2018/utils"
	"fmt"
	"strconv"
)

func main() {
	data := utils.LoadInput("11_1/input.txt")
	_, x, y := GetLargestPowerLevel(data[0], 300, 300)
	fmt.Printf("%d,%d\n", x, y)
}

// GetLargestPowerLevel returns the appropriate power level in the grid
func GetLargestPowerLevel(input string, gridY, gridX int) (int, int, int) {
	serialNumber, _ := strconv.Atoi(input)
	matrix := generatePowerLevelGrid(serialNumber, gridY, gridX)
	result, x, y := findLargestGridSumCoordinate(matrix, gridY, gridX, 3, 3)
	return result, x, y
}

func generatePowerLevelGrid(serialNumber, height, width int) [][]int {
	matrix := make([][]int, height)
	for y := range matrix {
		matrix[y] = make([]int, width)
		for x := range matrix[y] {
			matrix[y][x] = CalculatePowerLevel(serialNumber, y+1, x+1)
		}
	}
	return matrix
}

func findLargestGridSumCoordinate(matrix [][]int, height, width, convGridY, convGridX int) (int, int, int) {
	max, maxTopLeftY, maxTopLeftX := 0, 0, 0

	for y := 0; y <= height-convGridY; y++ {
		for x := 0; x <= width-convGridX; x++ {
			sum := 0
			for convY := 0; convY < convGridY; convY++ {
				for convX := 0; convX < convGridX; convX++ {
					sum += matrix[y+convY][x+convX]
				}
			}
			if sum > max {
				max = sum
				maxTopLeftX = x + 1
				maxTopLeftY = y + 1
			}
		}
	}
	return max, maxTopLeftX, maxTopLeftY
}

/*CalculatePowerLevel counts the result by the task definition
- Find the fuel cell's rack ID, which is its X coordinate plus 10.
- Begin with a power level of the rack ID times the Y coordinate.
- Increase the power level by the value of the grid serial number (your puzzle input).
- Set the power level to itself multiplied by the rack ID.
- Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
- Subtract 5 from the power level
*/
func CalculatePowerLevel(serialNumber, y, x int) int {
	rackID := x + 10
	return ((((rackID*y)+serialNumber)*rackID)%1000)/100 - 5
}
