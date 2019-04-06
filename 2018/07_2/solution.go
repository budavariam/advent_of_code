package main

import (
	"container/heap"
	"fmt"
	"regexp"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("07_2")
	result := MeasureFinishTime(data, 5)
	fmt.Println(result)
}

// MeasureFinishTime gets how long does it take to finish the work with n workers
func MeasureFinishTime(input []string, workercount int) int {
	nodes, startNodes := parseData(input)
	length := len(input)
	result := make([]string, length)
	resultIndex := 0
	currentTime := 0
	pq := priQueueFromNodes(nodes, startNodes)
	freeWorkers := workercount
	for pq.Len() > 0 {
		item := heap.Pop(pq).(*Item)
		freeWorkers--
		if freeWorkers == 0 {
			currentTime = item.estimatedFinish
			freeWorkers = 1
		}
		result[resultIndex] = item.value.id
		resultIndex++
		for _, chID := range item.value.out {
			child := nodes[chID]
			child.inCount--
			if child.inCount == 0 {
				heap.Push(pq, &Item{
					value:           child,
					priority:        int(chID[0]),
					estimatedFinish: calcEstimation(chID[0], item.estimatedFinish),
				})
			}
		}

	}
	return currentTime
}

// parseData builds a map with the nodes and a set with the start nodes
func parseData(input []string) (map[string]*Node, map[string]bool) {
	regex := *regexp.MustCompile(`Step (\w) must be finished before step (\w) can begin.`)
	nodes := map[string]*Node{}
	startNodes := map[string]bool{}
	for _, line := range input {
		parsedData := regex.FindStringSubmatch(line)
		from, to := parsedData[1], parsedData[2]
		if _, exists := nodes[from]; !exists {
			nodes[from] = &Node{id: from, out: make([]string, 0)}
			startNodes[from] = true
		}
		if _, exists := nodes[to]; !exists {
			nodes[to] = &Node{id: to, out: make([]string, 0), inCount: 1}
		} else {
			nodes[to].inCount++
		}
		nodes[from].out = append(nodes[from].out, to)
		delete(startNodes, to)
	}
	return nodes, startNodes
}

func priQueueFromNodes(nodes map[string]*Node, startNodes map[string]bool) *PriorityQueue {
	pq := make(PriorityQueue, len(startNodes))
	i := 0
	for id := range startNodes {
		pq[i] = &Item{
			value:           nodes[id],
			priority:        int(id[0]),
			index:           i,
			estimatedFinish: calcEstimation(id[0], 0),
		}
		i++
	}
	heap.Init(&pq)
	return &pq
}

func calcEstimation(id byte, currentTime int) int {
	return int(id+1-'A') + currentTime + 60
}
