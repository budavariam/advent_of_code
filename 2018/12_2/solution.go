package main

import (
	"fmt"
	"regexp"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("12_2")
	result := CountPlantsAfterNGenerations(data, 50000000000)
	fmt.Println(result)
}

// CountPlantsAfterNGenerations gets the number of plants after a paramterized number of generations
func CountPlantsAfterNGenerations(data []string, generationNumber int) int {
	state, ruleMatcher := parseData(data)
	prev, current, diff, generation := state.CountSumOfFilledPots(), 0, 0, 0
	for generation = 1; generation <= generationNumber; generation++ {
		newState := Strip{}
		newState.highestIndex = state.highestIndex
		newState.data = map[int]uint{}
		first := false
		// since I start from lowest-2, the first 4 elements are definitely 0 in the beginning
		key := state.data[state.lowestIndex] << 4
		for i := state.lowestIndex - 2; i <= state.highestIndex+2; i++ {
			if ruleMatcher.data[key] {
				if !first {
					// strip starting zeroes from the result set
					newState.lowestIndex = i
				} else if i > state.highestIndex {
					newState.highestIndex = i
				}
				newState.data[i] = 1
				first = true
			}
			// step with the binary number one to the left and add the next flag to the end
			key >>= 1
			key |= state.data[i+3] << 4
		}
		state = newState
		current = state.CountSumOfFilledPots()
		if diff == current-prev {
			// after a while the pattern starts to repeat itself
			break
		} else {
			diff = current - prev
			prev = current
		}
	}
	// the difference will be a constant from now on, so I can calculate the result of the remaining iterations and add the current count to it
	return (generationNumber-generation)*diff + current
}

func parseData(data []string) (Strip, Rule) {
	initialState := NewStrip(data[0][15:]) // magic15 == len("initial state: ")
	ruleMatcher := Rule{}
	ruleMatcher.data = map[uint]bool{}
	regex := *regexp.MustCompile(`([#.]{5}) => ([#.])`)
	for i := 2; i < len(data); i++ {
		rule := regex.FindStringSubmatch(data[i])
		res := rule[2] == "#"
		var j, key uint
		key = 0
		for j = 0; j < 5; j++ {
			// the length of the rules are always 5, lowest bit is the leftmost character in the rule
			if rule[1][j] == '#' {
				key |= 1 << j
			}
		}
		// use a bit pattern of an uint instead of a string as a key
		ruleMatcher.data[key] = res
	}
	return initialState, ruleMatcher
}

// Strip contains the plant pots
type Strip struct {
	data         map[int]uint
	lowestIndex  int
	highestIndex int
	currentIndex int
}

// NewStrip initializes a strip from an initial state
func NewStrip(initialState string) Strip {
	result := Strip{}
	result.data = map[int]uint{}
	result.highestIndex = len(initialState)
	for index, char := range initialState {
		if char == '#' {
			result.data[index] = 1
		}
	}
	return result
}

// CountSumOfFilledPots sums the number of the index of the pots that contain a plant
func (s Strip) CountSumOfFilledPots() int {
	count := 0
	for index := s.lowestIndex; index <= s.highestIndex; index++ {
		if s.data[index] > 0 {
			count += index
		}
	}
	return count
}

// PrintPlants prints the current strip
func (s Strip) PrintPlants() {
	for index := s.lowestIndex; index <= s.highestIndex; index++ {
		if s.data[index] > 0 {
			fmt.Print("#")
		} else {
			fmt.Print(".")
		}
	}
	fmt.Print("\n")
}

// Rule checks if the next generation will have a plant at this spot
type Rule struct {
	data map[uint]bool
}
