package main

import (
	"advent_of_code/2018/utils"
	"fmt"
)

func main() {
	data := utils.LoadInput("05_1/input.txt")
	result := LengthAfterReactions(data[0])
	fmt.Println(result)
}

// LengthAfterReactions plays the reactions in the polimer and returns its final length
func LengthAfterReactions(polymer string) int {
	var stack []rune
	n := 0
	for _, char := range polymer {
		if n > 0 && stack[n-1] == swapPolarity(char) {
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
