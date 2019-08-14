package main

import (
	"fmt"
	"regexp"
	"strconv"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	input := utils.LoadInput("23_1")
	result := EET(input)
	fmt.Println(result)
}

// EET gets the strongest bot and counts how many nanobots are in range of it
func EET(input []string) int {
	nanobots, carta := parseInput(input)
	var maxRadiusBot nanoBot
	for _, bot := range nanobots {
		if bot.radius > maxRadiusBot.radius {
			maxRadiusBot = bot
		}
	}
	return carta.CountBotsInRange(maxRadiusBot)
}

func parseInput(input []string) ([]nanoBot, cartograph) {
	regexBot := *regexp.MustCompile(`^pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)$`)
	nanobots := make([]nanoBot, len(input))
	carta := cartograph{}
	for lineNr, line := range input {
		rawBot := regexBot.FindStringSubmatch(line)
		botX, _ := strconv.Atoi(rawBot[1])
		botY, _ := strconv.Atoi(rawBot[2])
		botZ, _ := strconv.Atoi(rawBot[3])
		botRadius, _ := strconv.Atoi(rawBot[4])
		bot := nanoBot{radius: botRadius, position: coord{botX, botY, botZ}}
		nanobots[lineNr] = bot
		carta[bot.position] = &bot
	}
	return nanobots, carta
}

type nanoBot struct {
	radius   int
	position coord
}
type coord [3]int

func (c coord) calcManhattanDistance(other coord) int {
	dst := 0
	for i, val := range c {
		dst += abs(val - other[i])
	}
	return dst
}

type cartograph map[coord]*nanoBot

func (c cartograph) CountBotsInRange(bot nanoBot) int {
	count := 0
	for _, other := range c {
		if bot.position.calcManhattanDistance(other.position) <= bot.radius {
			count++
		}
	}

	return count
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
