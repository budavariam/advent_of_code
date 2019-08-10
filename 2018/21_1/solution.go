package main

import (
	"fmt"
	"os"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("21_1")
	ReverseEngineer(data)

	ChronalConversion(data)
}

// ReverseEngineer produces readable machine code
func ReverseEngineer(data []string) {
	ipBoundTo, instructions := ParseData(data)
	device := DeviceConverter{
		instructions: instructions,
		ipBoundTo:    ipBoundTo,
	}
	device.registers[0] = 1
	for i, instr := range instructions {
		instr.print(i)
	}
	fmt.Println("-------")
}

// ChronalConversion is the solution to the problem
func ChronalConversion(data []string) int {
	ipBoundTo, instructions := ParseData(data)
	device := Device{
		instructions: instructions,
		ipBoundTo:    ipBoundTo,
	}
	for {
		nextState, halt := device.nextInstruction()

		if device.ip == 28 {
			fmt.Println("Register state when hit the line which checks for exit condition:", nextState.registers, device.ip)
			fmt.Println(nextState.registers[3])

			os.Exit(0)
		}

		if halt {
			break
		}
		device = nextState
	}
	return device.registers[0]
}
