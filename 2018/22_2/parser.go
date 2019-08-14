package main

import (
	"regexp"
	"strconv"
)

func parseInput(data []string) (int, coord) {
	regexDepth := *regexp.MustCompile(`\w+: (\d+)`)

	rawDepth := regexDepth.FindStringSubmatch(data[0])
	depth, _ := strconv.Atoi(rawDepth[1])
	regexCoord := *regexp.MustCompile(`\w+: (\d+),(\d+)`)
	rawTarget := regexCoord.FindStringSubmatch(data[1])
	targetX, _ := strconv.Atoi(rawTarget[1])
	targetY, _ := strconv.Atoi(rawTarget[2])
	target := coord{X: targetX, Y: targetY}

	return depth, target
}
