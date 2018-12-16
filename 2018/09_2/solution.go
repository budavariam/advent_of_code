package main

import (
	"advent_of_code/2018/utils"
	"fmt"
	"regexp"
	"strconv"
)

func main() {
	data := utils.LoadInput("09_1/input.txt")
	result := WinnersScore(data[0])
	fmt.Println(result)
}

// WinnersScore gets the highest score from the elves game
func WinnersScore(data string) int {
	regex := *regexp.MustCompile(`(\d+).*?(\d+)`)
	parsedData := regex.FindStringSubmatch(data)
	playerCount, _ := strconv.Atoi(parsedData[1])
	lastMarble, _ := strconv.Atoi(parsedData[2])
	scores := make([]int, playerCount)
	marbleIndex := 1
	playerIndex := 0
	currentMarble := &marble{nil, nil, 0}
	currentMarble.cw = currentMarble
	currentMarble.ccw = currentMarble
	//firstMarble := currentMarble
	var gotScore int
	for {
		if marbleIndex > 0 && marbleIndex%23 == 0 {
			currentMarble, gotScore = currentMarble.multipleOf23(marbleIndex)
			scores[playerIndex] += gotScore
		} else {
			currentMarble = currentMarble.pushNew(marbleIndex)
		}
		if marbleIndex == lastMarble*100 {
			break
		}
		marbleIndex++
		playerIndex++
		if playerIndex == playerCount {
			playerIndex = 0
		}
		//firstMarble.printPlayground()
	}
	return getMaxScore(scores)
}

type marble struct {
	cw    *marble
	ccw   *marble
	value int
}

func (m *marble) pushNew(newIndex int) *marble {
	newMarble := &marble{cw: m.cw.cw, ccw: m.cw, value: newIndex}
	m.cw.cw.ccw = newMarble
	m.cw.cw = newMarble
	return newMarble
}

func (m *marble) multipleOf23(newIndex int) (*marble, int) {
	//First, the current player keeps the marble they would have placed, adding it to their score. In addition, the marble 7 marbles counter-clockwise from the current marble is removed from the circle and also added to the current player's score. The marble located immediately clockwise of the marble that was removed becomes the new current marble.
	for i := 0; i < 7; i++ {
		m = m.ccw
	}
	score := newIndex + m.value
	m.cw.ccw = m.ccw
	m.ccw.cw = m.cw
	return m.cw, score
}

func (m *marble) printPlayground() {
	stop := m.value
	for {
		fmt.Print(m.value, " ")
		m = m.cw
		if m.value == stop {
			break
		}
	}
	fmt.Print("\n")
}

func getMaxScore(scores []int) int {
	max := 0
	for _, score := range scores {
		if score > max {
			max = score
		}
	}
	return max
}
