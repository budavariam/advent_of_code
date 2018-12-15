package main

import (
	"advent_of_code/2018/utils"
	"fmt"
	"strconv"
	"strings"
)

func main() {
	data := utils.LoadInput("08_2/input.txt")
	result := RootValue(data)
	fmt.Println(result)
}

// RootValue gets the value of the root node
func RootValue(data []string) int {
	splittedText := strings.Split(data[0], " ")
	numbers := make([]int, len(splittedText))
	for i, n := range splittedText {
		numbers[i], _ = strconv.Atoi(n)
	}
	tree, _ := buildTree(0, numbers)
	return tree.value()
}

// buildTree is a recursive function to build the tree hierarchy
func buildTree(index int, numbers []int) (*Tree, int) {
	var child *Tree
	childCount := numbers[index]
	metadataCount := numbers[index+1]
	index += 2
	tree := &Tree{children: make([]*Tree, 0), metadataSum: 0, metadata: make([]int, 0)}
	for i := 0; i < childCount; i++ {
		child, index = buildTree(index, numbers)
		tree.children = append(tree.children, child)
	}
	sum := 0
	for _, number := range numbers[index : index+metadataCount] {
		sum += number
	}
	tree.metadata = numbers[index : index+metadataCount]
	tree.metadataSum = sum
	tree.childCount = childCount
	return tree, index + metadataCount
}

// Tree contains the memory tree
type Tree struct {
	children    []*Tree
	metadata    []int
	metadataSum int
	childCount  int
}

// value adds the sum of metadata if it doesn't have childnodes, otherwise metadata becomes an index list and it adds up the values of those child nodes
func (node Tree) value() int {
	cache := map[int]int{}
	if node.childCount > 0 {
		sum := 0
		for _, childIndex := range node.metadata {
			if childIndex <= node.childCount {
				if val, exists := cache[childIndex]; exists {
					sum += val
				} else {
					val := node.children[childIndex-1].value()
					cache[childIndex] = val
					sum += val
				}
			}
		}
		return sum
	}
	return node.metadataSum
}
