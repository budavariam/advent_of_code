package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("19_1")
	result := GoWithTheFlow(data)
	fmt.Println(result)
}

// GoWithTheFlow is the solution to the problem
func GoWithTheFlow(data []string) int {
	ipBoundTo, instructions := ParseData(data)
	device := Device{
		instructions: instructions,
		ipBoundTo:    ipBoundTo,
	}
	for {
		nextState, halt := device.nextInstruction()
		if halt {
			break
		}
		device = nextState
	}
	return device.registers[0]
}
