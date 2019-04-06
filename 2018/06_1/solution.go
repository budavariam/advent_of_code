package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("06_1")
	result := GetMaximalInnerArea(data)
	fmt.Println(result)
}

// GetMaximalInnerArea counts the largest area inside the convex hull of the points
func GetMaximalInnerArea(input []string) int {
	coords, boundaries := normalizeCoords(input)
	return getLargestArea(coords, boundaries)
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

type matrixnode struct {
	closestpointID int
	distance       int
	visited        bool
}

type queueitem struct {
	point    point
	distance int
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

// calculates the largest inner area in the matrix
func getLargestArea(coords []point, boundaries bounds) int {
	matrix := initMatrix(boundaries.maxx, boundaries.maxy)
	queue := make([]queueitem, 0)
	for _, coord := range coords {
		newNode := matrix[coord.y][coord.x]
		newNode.closestpointID = coord.id
		newNode.distance = 0
		newNode.visited = true
		matrix[coord.y][coord.x] = newNode
		queue = append(queue, queueitem{point: coord, distance: 0})
	}
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:] //pop left
		queue = fillManhattan(matrix, curr, boundaries, queue)
	}
	infinites := getInfiniteAreas(matrix, boundaries)
	counter := countAreasExceptIn(matrix, infinites)
	return maxIntFromMapValues(counter)
}

// initMatrix initializes a 2d slice with initial values.
func initMatrix(width int, height int) [][]matrixnode {
	matrix := make([][]matrixnode, height)
	for y := 0; y < height; y++ {
		matrix[y] = make([]matrixnode, width)
		for x := 0; x < width; x++ {
			matrix[y][x] = matrixnode{closestpointID: -1, distance: -1, visited: false}
		}
	}
	return matrix
}

// maxIntFromMapValues gets the max integer value from a map
func maxIntFromMapValues(data map[int]int) int {
	maxVal := 0
	for _, value := range data {
		if maxVal < value {
			maxVal = value
		}
	}
	return maxVal
}

// countAreasExceptIn counts the number of areas with a specific id, except the ones provided in a 'set'
func countAreasExceptIn(matrix [][]matrixnode, except map[int]bool) map[int]int {
	counter := map[int]int{}
	for _, line := range matrix {
		for _, elem := range line {
			if !except[elem.closestpointID] {
				counter[elem.closestpointID]++
			}
		}
	}
	return counter
}

// printMatrix prints the contents of the matrix mostly for debug purposes
func printMatrix(matrix [][]matrixnode, boundaries bounds) {
	for y := 0; y < boundaries.maxy; y++ {
		for x := 0; x < boundaries.maxx; x++ {
			current := matrix[y][x]
			if !current.visited {
				fmt.Printf("x   (%02d), ", current.distance)
			} else if current.closestpointID < 0 {
				fmt.Printf(".   (%02d), ", current.distance)
			} else {
				fmt.Printf("%03d (%02d), ", current.closestpointID, current.distance)
			}
		}
		fmt.Print("\n")
	}
	fmt.Println("***")
}

// fillManhattan implements breadth first search logic for the task
func fillManhattan(matrix [][]matrixnode, current queueitem, boundaries bounds, queue []queueitem) []queueitem {
	directions := [][]int{[]int{0, 1}, []int{1, 0}, []int{0, -1}, []int{-1, 0}}
	for _, dir := range directions {
		y, x := current.point.y+dir[0], current.point.x+dir[1]
		insideBounds := y >= 0 && y < boundaries.maxy && x >= 0 && x < boundaries.maxx
		if insideBounds {
			newNode := matrix[y][x]
			if !newNode.visited ||
				newNode.visited && newNode.closestpointID != current.point.id && newNode.distance == current.distance+1 {
				// haven't been there or been there with less distance
				newNode.distance = current.distance + 1
				if newNode.visited && newNode.closestpointID != current.point.id && newNode.distance == current.distance+1 {
					newNode.closestpointID = -1
				} else {
					newNode.closestpointID = current.point.id
				}
				newNode.visited = true
				matrix[y][x] = newNode
				queue = append(queue, queueitem{point: point{x: x, y: y, id: current.point.id}, distance: current.distance + 1})
			}
		}
	}
	return queue
}

// getInfiniteAreas collects the areaids that touch the boundaries
func getInfiniteAreas(matrix [][]matrixnode, boundaries bounds) map[int]bool {
	infinites := map[int]bool{}
	for y, line := range matrix {
		if y == 0 || y == boundaries.maxy-1 {
			for x, elem := range line {
				if x == 0 || x == boundaries.maxx-1 && elem.closestpointID > -1 {
					infinites[elem.closestpointID] = true
				}
			}
		}
	}
	return infinites
}
