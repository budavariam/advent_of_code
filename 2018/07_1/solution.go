package main

import (
	"advent_of_code/2018/utils"
	"container/heap"
	"fmt"
	"regexp"
	"strings"
)

func main() {
	data := utils.LoadInput("07_1/input.txt")
	result := TopologicalSort(data)
	fmt.Println(result)
}

// TopologicalSort orders the nodes topologically, resolves ambiguity by lexicographical ordering
func TopologicalSort(input []string) string {
	nodes, startNodes := parseData(input)
	result := make([]string, len(input))
	resultIndex := 0
	pq := priQueueFromNodes(nodes, startNodes)
	for pq.Len() > 0 {
		item := heap.Pop(pq).(*Item)
		result[resultIndex] = item.value.id
		resultIndex++
		for _, chID := range item.value.out {
			child := nodes[chID]
			child.inCount--
			if child.inCount == 0 {
				heap.Push(pq, &Item{value: child, priority: int(chID[0])})
			}
		}

	}
	return strings.Join(result, "")
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
			value:    nodes[id],
			priority: int(id[0]),
			index:    i,
		}
		i++
	}
	heap.Init(&pq)
	return &pq
}
