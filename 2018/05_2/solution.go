package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("05_1")
	result := MinimalPolimer(data[0])
	fmt.Println(result)
}

// MinimalPolimer will return the least possible polimer by this elimination rule by eliminating one type of polimer completely
func MinimalPolimer(data string) int {
	minimalLength := len(data)
	for _, char := range "abcdefghijklmnopqrstuvwxyz" {
		current := LengthAfterReactions(data, char)
		if current < minimalLength {
			minimalLength = current
		} else if current == 0 {
			return 0
		}
	}
	return minimalLength

}

// LengthAfterReactions plays the reactions in the polimer and returns its final length
func LengthAfterReactions(polymer string, ignore rune) int {
	var stack []rune
	n := 0
	for _, char := range polymer {
		if char == ignore || char == swapPolarity(ignore) {
			continue
		} else if n > 0 && stack[n-1] == swapPolarity(char) {
			/* if the current char is in the stack with a different polarity, pop the last char from stack,
			by not adding it to the stack, it eliminates the previous and the current as well. */
			stack = stack[:n-1]
			n--
		} else {
			stack = append(stack, char)
			n++
		}
	}
	return n
}

func swapPolarity(char rune) rune {
	if char <= 'Z' && char >= 'A' {
		return char - 'A' + 'a'
	}
	return char - 'a' + 'A'
}
