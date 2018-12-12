package main

import (
	"advent_of_code/2018/utils"
	"fmt"
	"regexp"
	"strings"
)

func main() {
	data := utils.LoadInput("12_1/input.txt")
	result := CountPlantsAfterNGenerations(data, 20)
	fmt.Println(result)
}

// CountPlantsAfterNGenerations gets the number of plants after a paramterized number of generations
func CountPlantsAfterNGenerations(data []string, generationNumber int) int {
	state, ruleMatcher := parseData(data)
	for i := 0; i < generationNumber; i++ {
		newState := Strip{}
		newState.lowestIndex = state.lowestIndex
		newState.highestIndex = state.highestIndex
		newState.data = map[int]bool{}
		for i := state.lowestIndex - 2; i <= state.highestIndex+2; i++ {
			s := state.data
			if ruleMatcher.ApplyRule(s[i-2], s[i-1], s[i], s[i+1], s[i+2]) {
				if i < state.lowestIndex {
					newState.lowestIndex = i
				} else if i > state.highestIndex {
					newState.highestIndex = i
				}
				newState.data[i] = true
			} else {
				newState.data[i] = false
			}
		}
		state = newState
	}
	return state.CountSumOfFilledPots()
}

func parseData(data []string) (Strip, Rule) {
	initialState := NewStrip(data[0][15:]) // magic15 == len("initial state: ")
	ruleMatcher := Rule{}
	ruleMatcher.data = map[string]bool{}
	regex := *regexp.MustCompile(`([#.]{5}) => ([#.])`)
	for i := 2; i < len(data); i++ {
		rule := regex.FindStringSubmatch(data[i])
		res := rule[2] == "#"
		ruleMatcher.data[rule[1]] = res
	}
	return initialState, ruleMatcher
}

// Strip contains the plant pots
type Strip struct {
	data         map[int]bool
	lowestIndex  int
	highestIndex int
	currentIndex int
}

// NewStrip initializes a strip from an initial state
func NewStrip(initialState string) Strip {
	result := Strip{}
	result.data = map[int]bool{}
	result.highestIndex = len(initialState)
	for index, char := range initialState {
		if char == '#' {
			result.data[index] = true
		}
	}
	return result
}

// CountSumOfFilledPots sums the number of the index of the pots that contain a plant
func (s Strip) CountSumOfFilledPots() int {
	count := 0
	for index := s.lowestIndex; index <= s.highestIndex; index++ {
		if s.data[index] {
			count += index
		}
	}
	return count
}

// PrintPlants prints the current strip
func (s Strip) PrintPlants() {
	for index := s.lowestIndex; index <= s.highestIndex; index++ {
		if s.data[index] {
			fmt.Print("#")
		} else {
			fmt.Print(".")
		}
	}
	fmt.Print("\n")
}

// Rule checks if the next generation will have a plant at this spot
type Rule struct {
	data map[string]bool
}

// ApplyRule checks the result of the current state
func (r Rule) ApplyRule(l2, l1, c, r1, r2 bool) bool {
	key := strings.Join([]string{f(l2), f(l1), f(c), f(r1), f(r2)}, "")
	return r.data[key]
}

// f converts a bool value to a string
func f(input bool) string {
	if input {
		return "#"
	} else {
		return "."
	}
}
