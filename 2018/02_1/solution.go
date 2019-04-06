package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("02_1")
	result := MultiplyCountedwords(data)
	fmt.Println(result)
}

func getWordHistogram(word string) map[rune]int {
	histogram := make(map[rune]int)
	for _, char := range word {
		histogram[char]++
	}
	return histogram
}

func hasExactNumber(histogram map[rune]int, count int) int {
	for _, value := range histogram {
		if value == count {
			return 1
		}
	}
	return 0
}

// MultiplyCountedwords multiplies the number of words that has exactly 2 and 3 matches.
func MultiplyCountedwords(data []string) int {
	hasExactly2 := 0
	hasExactly3 := 0
	for _, word := range data {
		wordhistogram := getWordHistogram(word)
		hasExactly2 += hasExactNumber(wordhistogram, 2)
		hasExactly3 += hasExactNumber(wordhistogram, 3)
	}
	return hasExactly2 * hasExactly3
}
