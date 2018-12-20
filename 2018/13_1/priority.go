// source: https://golang.org/pkg/container/heap/

// This example demonstrates a priority queue built using the heap interface.
package main

import (
	"container/heap"
)

// An Item is something we manage in a priority.
type Item struct {
	value *Cart // The value of the item; arbitrary.
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

// A Priority implements heap.Interface and holds Items.
type Priority []*Item

func (pq Priority) Len() int { return len(pq) }

func (pq Priority) Less(j, i int) bool {
	if pq[i].value.posY == pq[j].value.posY {
		return pq[i].value.posX > pq[j].value.posX
	}
	return pq[i].value.posY > pq[j].value.posY
}

func (pq Priority) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

// Push an item to the list
func (pq *Priority) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

// Pop an item from the list
func (pq *Priority) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[0]
	item.index = -1 // for safety
	*pq = old[1:n]
	return item
}

// Update modifies the value of an Item in the list.
func (pq *Priority) Update(item *Item, value *Cart, priority int) {
	item.value = value
	heap.Fix(pq, item.index)
}
