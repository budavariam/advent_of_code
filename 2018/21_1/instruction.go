package main

import (
	"fmt"
	"strconv"
	"strings"
)

// Instruction can be used in the device
type Instruction struct {
	opName string
	Ain    int
	Bin    int
	Cout   int
}

func (i Instruction) init(raw string) Instruction {
	splitted := strings.Split(raw, " ")
	i.opName = splitted[0]
	i.Ain, _ = strconv.Atoi(splitted[1])
	i.Bin, _ = strconv.Atoi(splitted[2])
	i.Cout, _ = strconv.Atoi(splitted[3])
	return i
}

func (i Instruction) print(lineNum int) {
	fmt.Printf("%d\t", lineNum)
	operationsConvertMapping[i.opName](i, lineNum)
}
