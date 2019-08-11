package main

import (
	"fmt"
	"os"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("21_2")
	result := ReverseEngineeredCode(data)
	// result := SimulateOnDevice(data)
	fmt.Println(result)
}

// ReverseEngineeredCode is the code that runs on the device without getting into an infinite loop
func ReverseEngineeredCode(data []string) int {
	a, c, d, init, prev := 0, 0, 0, true, -1
	visited := map[int]bool{}

	for init || d != a {
		init = false

		c = d | 0x10000
		d = 14070682
		for {
			d = (((d + (c & 0xFF)) & 0xFFFFFF) * 65899) & 0xFFFFFF
			if 256 > c {
				break
			}
			c = c / 256
		}
		if !visited[d] {
			visited[d] = true
			prev = d
		} else {
			return prev
		}
	}
	return -1
}

// SimulateOnDevice is the solution to the problem
func SimulateOnDevice(data []string) int {
	ipBoundTo, instructions := ParseData(data)
	device := Device{
		instructions: instructions,
		ipBoundTo:    ipBoundTo,
	}
	foundValues := map[int]bool{}
	prev := -1
	cnt := 0
	for {
		nextState, halt := device.nextInstruction()
		//fmt.Println(device.ip, nextState.registers)
		if device.ip == 28 {
			cnt++
			fmt.Println(cnt, nextState.registers[3])
			if cnt%1000 == 0 {
				fmt.Println(cnt)
			}
			registerValue := nextState.registers[3]
			if !foundValues[registerValue] {
				foundValues[registerValue] = true
				prev = registerValue
			} else {
				fmt.Println("The last value before repetition is: ", prev)
				os.Exit(0)
			}
		}

		if halt {
			break
		}
		device = nextState
	}
	return device.registers[0]
}
