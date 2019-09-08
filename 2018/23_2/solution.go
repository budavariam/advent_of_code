package main

import (
	"container/heap"
	"fmt"
	"regexp"
	"strconv"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	input := utils.LoadInput("23_2")
	result := LNN(input)
	fmt.Println(result)
}

// LNN gets the closest point that has the largest number of nanobot intersections. Based on a solution from reddit.
//   For each bot, the code calculates d = manhattan distance to origin and adds (MAX(d-r,0), 1) and (d+r, -1) to a priority queue.
//   The queue is holding entries for the start and end of each "line segment" as measured by manhattan distance from the origin. At the start of the segment the 1 adds to the total of overlapping segments. The -1 that marks the segment's end, and is used to decrease the counter.
//   The final loop calculates the maximum number of overlapping segments, and the point where the maximum is hit, which is the answer.
//   This is really a very nice and amazingly simple solution! Thanks, /u/EriiKKo
func LNN(input []string) int {
	nanobots := parseInput(input)
	queue := priQueueFromBots(nanobots)

	count, maxCount, result := 0, 0, 0
	for queue.Len() > 0 {

		current := heap.Pop(queue).(*Item)
		count += current.value
		if count > maxCount {
			result = current.priority
			maxCount = count
		}
	}
	return result
}

func priQueueFromBots(nanobots []nanoBot) *PriorityQueue {
	pq := make(PriorityQueue, (len(nanobots))*2)

	for i, b := range nanobots {
		d := abs(b.position[0]) + abs(b.position[1]) + abs(b.position[2])

		pq[2*i] = &Item{
			priority: max(0, d-b.radius),
			value:    1,
		}
		pq[2*i+1] = &Item{
			priority: d + b.radius + 1,
			value:    -1,
		}
	}
	heap.Init(&pq)
	return &pq
}

func parseInput(input []string) []nanoBot {
	regexBot := *regexp.MustCompile(`^pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)$`)
	nanobots := make([]nanoBot, len(input))
	for lineNr, line := range input {
		rawBot := regexBot.FindStringSubmatch(line)
		botX, _ := strconv.Atoi(rawBot[1])
		botY, _ := strconv.Atoi(rawBot[2])
		botZ, _ := strconv.Atoi(rawBot[3])
		botRadius, _ := strconv.Atoi(rawBot[4])
		bot := nanoBot{radius: botRadius, position: coord{botX, botY, botZ}}
		nanobots[lineNr] = bot
	}
	return nanobots
}

type nanoBot struct {
	radius   int
	position coord
}
type coord [3]int

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}
