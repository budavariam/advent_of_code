package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("19_1")
	ReverseEngineer(data)
	fmt.Println(GoWithTheFlow())
}

// ReverseEngineer produces readable machine code
func ReverseEngineer(data []string) {
	ipBoundTo, instructions := ParseData(data)
	device := Device{
		instructions: instructions,
		ipBoundTo:    ipBoundTo,
	}
	device.registers[0] = 1
	for i, instr := range instructions {
		instr.print(i)
	}
}

//GoWithTheFlow the reverse engineered and improved code from the device
func GoWithTheFlow() int {
	a := 1
	b := 0
	c := 128
	f := 836 + c
	if a == 1 {
		c = 10550400
		f = f + c
		a = 0
	}
	for b = 1; b <= f+1; b++ {
		if (f % b) == 0 {
			a += b
		}
	}
	return a
}
