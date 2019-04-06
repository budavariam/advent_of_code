package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("14_2")
	result := RecipeCountBeforeValue(data[0])
	fmt.Println(result)
}

// RecipeCountBeforeValue gets how many recipes appear before the value
func RecipeCountBeforeValue(data string) string {
	scoreboard := &recipe{&recipe{nil, 7}, 3} // keep the reference to the start
	scoreboard.next.next = scoreboard         //create a circular singly linked list
	endOfScoreboard := scoreboard.next        // keep track of the end of the scoreboard to append to it
	nbeforeTheEnd := scoreboard
	checkindex := 0
	resultCheckInitialized := false
	firstElf := scoreboard
	secondElf := scoreboard.next
	length := 2
	//i := 0
	var move int
	inputLength := len(data)
	//printScoreboard(i, length, scoreboard, endOfScoreboard, nbeforeTheEnd, firstElf, secondElf)
findRecipe:
	for {
		if !resultCheckInitialized && length > inputLength {
			checkindex := length - inputLength
			nbeforeTheEnd.moveForward(checkindex)
			resultCheckInitialized = true
		}
		newSum := firstElf.value + secondElf.value
		endOfScoreboard, move = endOfScoreboard.pushNewRecipes(newSum)
		length += move
		firstElf = firstElf.moveForward(1 + firstElf.value)
		secondElf = secondElf.moveForward(1 + secondElf.value)
		if resultCheckInitialized {
			for moveForward := 0; moveForward < move; moveForward++ {
				nbeforeTheEnd = nbeforeTheEnd.moveForward(1)
				checkindex++
				if check := nbeforeTheEnd.getNAfter(inputLength, 0); check == data {
					break findRecipe
				}
			}
		}
		//i++
		//printScoreboard(i, length, scoreboard, endOfScoreboard, nbeforeTheEnd, firstElf, secondElf)
	}
	return fmt.Sprintf("%d", checkindex)
}

type recipe struct {
	next  *recipe
	value int
}

func (currentEnd *recipe) pushNewRecipes(newValue int) (*recipe, int) {
	scoreboardStart := currentEnd.next
	firstDigit := newValue / 10
	secondDigit := newValue % 10
	move := 1
	if newValue > 9 {
		currentEnd.next = &recipe{value: firstDigit, next: &recipe{value: secondDigit, next: scoreboardStart}}
		currentEnd = currentEnd.next.next
		move++
	} else {
		currentEnd.next = &recipe{value: newValue, next: scoreboardStart}
		currentEnd = currentEnd.next
	}
	return currentEnd, move
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

func printScoreboard(i, length int, start, end, endMarker, marker1, marker2 *recipe) {
	iterator := start
	fmt.Printf("%d {%d}: ", i, length)
	for {
		if iterator == endMarker {
			fmt.Printf(".")
		}
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
