package main

import (
	"advent_of_code/2018/utils"
	"fmt"
	"strconv"
	"strings"
)

func main() {
	data := utils.LoadInput("08_1/input.txt")
	result := SumMetadata(data)
	fmt.Println(result)
}

// SumMetadata adds up all metadata information in the tree
func SumMetadata(data []string) int {
	splittedText := strings.Split(data[0], " ")
	numbers := make([]int, len(splittedText))
	for i, n := range splittedText {
		numbers[i], _ = strconv.Atoi(n)
	}
	tree, _ := buildTree(0, numbers)
	sum := traverseTree(tree, func(node *Tree) int {
		sum := 0
		for _, number := range node.metadata {
			sum += number
		}
		return sum
	})
	return sum
}

// buildTree is a recursive function to build the tree hierarchy
func buildTree(index int, numbers []int) (*Tree, int) {
	var child *Tree
	childCount := numbers[index]
	metadataCount := numbers[index+1]
	index += 2
	tree := &Tree{children: make([]*Tree, 0), metadata: make([]int, 0)}
	for i := 0; i < childCount; i++ {
		child, index = buildTree(index, numbers)
		tree.children = append(tree.children, child)
	}
	tree.metadata = numbers[index : index+metadataCount]
	return tree, index + metadataCount
}

// Tree contains the memory tree
type Tree struct {
	children []*Tree
	metadata []int
}

func traverseTree(tree *Tree, visit func(*Tree) int) int {
	result := visit(tree)
	for _, node := range tree.children {
		result += traverseTree(node, visit)
	}
	return result
}
