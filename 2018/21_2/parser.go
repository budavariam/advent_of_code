package main

import (
	"strconv"
	"strings"
)

// ParseData loads the data from the input
func ParseData(raw []string) (int, []Instruction) {
	result := make([]Instruction, len(raw)-1)

	ipBoundTo := getInstructionPointerBound(raw[0])

	for lineNumber, rawInstruction := range raw[1:] {
		result[lineNumber] = Instruction{}.init(rawInstruction)
	}
	return ipBoundTo, result
}

func getInstructionPointerBound(line string) int {
	splitted := strings.Split(line, " ")
	ip, _ := strconv.Atoi(splitted[1])
	return ip
}
