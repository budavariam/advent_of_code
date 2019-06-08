package main

import (
	"strconv"
	"strings"
)

// Instruction can be used in the device
type Instruction struct {
	opCode int
	Ain    int
	Bin    int
	Cout   int
}

func (i Instruction) init(raw string) Instruction {
	splitted := strings.Split(raw, " ")
	i.opCode, _ = strconv.Atoi(splitted[0])
	i.Ain, _ = strconv.Atoi(splitted[1])
	i.Bin, _ = strconv.Atoi(splitted[2])
	i.Cout, _ = strconv.Atoi(splitted[3])
	return i
}
