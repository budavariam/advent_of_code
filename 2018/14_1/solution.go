package main

import (
	"fmt"
	"strconv"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("14_1")
	result := TenRecipeScores(data[0])
	fmt.Println(result)
}

// TenRecipeScores gets the ten recipes immediately after the numnber of recipes after my input
func TenRecipeScores(data string) string {
	numberOfRecipes, _ := strconv.Atoi(data)
	scoreboard := &recipe{&recipe{nil, 7}, 3} // keep the reference to the start
	scoreboard.next.next = scoreboard         //create a circular singly linked list
	endOfScoreboard := scoreboard.next        // keep track of the end of the scoreboard to append to it
	firstElf := scoreboard
	secondElf := scoreboard.next
	length := 2
	i := 0
	//printScoreboard(i, length, scoreboard, endOfScoreboard, firstElf, secondElf)
	for length < numberOfRecipes+10 {
		newSum := firstElf.value + secondElf.value
		endOfScoreboard, length = endOfScoreboard.pushNewRecipes(newSum, length)
		firstElf = firstElf.moveForward(1 + firstElf.value)
		secondElf = secondElf.moveForward(1 + secondElf.value)
		i++
		//printScoreboard(i, length, scoreboard, endOfScoreboard, firstElf, secondElf)
	}
	return scoreboard.getNAfter(10, numberOfRecipes)
}

type recipe struct {
	next  *recipe
	value int
}

func (currentEnd *recipe) pushNewRecipes(newValue int, length int) (*recipe, int) {
	scoreboardStart := currentEnd.next
	firstDigit := newValue / 10
	secondDigit := newValue % 10
	if newValue > 9 {
		currentEnd.next = &recipe{value: firstDigit, next: &recipe{value: secondDigit, next: scoreboardStart}}
		currentEnd = currentEnd.next.next
		length += 2
	} else {
		currentEnd.next = &recipe{value: newValue, next: scoreboardStart}
		currentEnd = currentEnd.next
		length++
	}
	return currentEnd, length
}

func (currentEnd *recipe) getNAfter(n int, after int) string {
	result := make([]rune, n)
	iterator := currentEnd
	for i := 0; i < after; i++ {
		iterator = iterator.next
	}
	for i := 0; i < n; i++ {
		result[i] = rune('0' + iterator.value)
		iterator = iterator.next
	}
	return string(result)
}

func (currentEnd *recipe) moveForward(n int) *recipe {
	iterator := currentEnd
	for i := 0; i < n; i++ {
		iterator = iterator.next
	}
	return iterator
}

func printScoreboard(i, length int, start, end, marker1, marker2 *recipe) {
	iterator := start
	fmt.Printf("%d {%d}: ", i, length)
	for {
		if iterator != marker1 && iterator != marker2 {
			fmt.Printf("%d ", iterator.value)
		} else if iterator == marker1 && iterator == marker2 {
			fmt.Printf("([%d]) ", iterator.value)
		} else if iterator == marker1 {
			fmt.Printf("(%d) ", iterator.value)
		} else if iterator == marker2 {
			fmt.Printf("[%d] ", iterator.value)
		}
		if iterator == end {
			break
		}
		iterator = iterator.next
	}
	fmt.Printf("\n")
}
