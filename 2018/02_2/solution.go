package main

import (
	"advent_of_code/2018/utils"
	"fmt"
)

func main() {
	data := utils.LoadInput("02_2/input.txt")
	result := GetClosestBoxes(data)
	fmt.Println(result)
}

// GetClosestBoxes returns the letters of the two words that differ by only one character.
func GetClosestBoxes(data []string) string {
	cache := make(map[string]bool)
	wordlength := len(data[0])
	for _, word := range data {
		possibilities := make([]string, wordlength)
		for i, char := range word {
			for j := 0; j < wordlength; j++ {
				// Get the different variations with one missing character from each word
				if i != j {
					possibilities[j] += string(char)
				}
			}
		}
		for _, newword := range possibilities {
			alreadyIn := cache[newword]
			if alreadyIn {
				return newword
			}
		}
		// Avoid getting false positive for duplicated chars next to each other
		for _, newword := range possibilities {
			cache[newword] = true
		}
	}
	return ""
}
