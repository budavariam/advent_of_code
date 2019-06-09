package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

// ChronalClassification is the solution to the problem
func ChronalClassification(data []string) int {
	observations, instructions := ParseData(data)
	opCodeMap := GetOpcodeMatrix(observations)
	device := Device{}
	for _, instr := range instructions {
		device = opCodeMap[instr.opCode](instr, device)
	}
	// fmt.Println("The final device result is:", device)
	return device[0]
}

func main() {
	data := utils.LoadInput("16_2")
	result := ChronalClassification(data)
	fmt.Println(result)
}
