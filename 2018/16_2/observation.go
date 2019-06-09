package main

import "regexp"

// Observation is collected to determine which opcode is which instruction
type Observation struct {
	before Device
	after  Device
	instr  Instruction
}

func (o *Observation) init(raw []string) {
	instr := Instruction{}
	o.instr = instr.init(raw[1])
	regex := *regexp.MustCompile(`\[(\d+), (\d+), (\d+), (\d+)\]`)
	o.before = initDevice(regex.FindStringSubmatch(raw[0])[1:5])
	o.after = initDevice(regex.FindStringSubmatch(raw[2])[1:5])

}

// createRandomOpcodeTable orders the instructions in an arbitrary order to make it easy to work with them
func createRandomOpcodeTable() map[int]func(Instruction, Device) Device {
	return map[int]func(Instruction, Device) Device{
		0:  addr,
		1:  addi,
		2:  mulr,
		3:  muli,
		4:  banr,
		5:  bani,
		6:  borr,
		7:  bori,
		8:  setr,
		9:  seti,
		10: gtir,
		11: gtri,
		12: gtrr,
		13: eqir,
		14: eqri,
		15: eqrr,
	}
}

// createValidOpcodeTable maps the operation codes to the random ordered initial instruction table
func createValidOpcodeTable(opcodeMapping map[int]int) map[int]func(Instruction, Device) Device {
	result := map[int]func(Instruction, Device) Device{}
	randomOpcodeMap := createRandomOpcodeTable()
	for validOpcode, keyInRandomOpcodes := range opcodeMapping {
		result[validOpcode] = randomOpcodeMap[keyInRandomOpcodes]
	}
	return result
}

// getOpcodeMapping figures out which opcode corresponds to which instruction
func getOpcodeMapping(which map[int]map[int]bool) map[int]int {
	result := map[int]int{}
	for r := 0; r < 16; r++ {
		for i, whichMap := range which {
			if len(whichMap) == 1 {
				for key := range whichMap {
					result[i] = key
				}
				delete(which, i)
				for _, otherOccurrences := range which {
					delete(otherOccurrences, result[i])
				}
			}
		}
	}
	// fmt.Println("The mapping of the random order: ", result)
	return result
}

// getPossibilityMatrix checks which opcodes act the same way in the observations
func getPossibilityMatrix(obs Observation) map[int]bool {
	possibilities := createRandomOpcodeTable()
	options := map[int]bool{}
	for pr, evaluator := range possibilities {
		res := evaluator(obs.instr, obs.before)
		if res.isEqual(obs.after) {
			options[pr] = true
		}
	}
	return options
}

// GetOpcodeMatrix matches the operations with the observations
func GetOpcodeMatrix(observations []Observation) map[int]func(Instruction, Device) Device {
	which := map[int]map[int]bool{}
	for i := 0; i <= 15; i++ {
		nth := map[int]bool{}
		for j := 0; j <= 15; j++ {
			nth[j] = true
		}
		which[i] = nth
	}
	for _, observation := range observations {
		matrix := getPossibilityMatrix(observation)
		which[observation.instr.opCode] = intersect(which[observation.instr.opCode], matrix)
	}
	eliminatedResult := getOpcodeMapping(which)
	return createValidOpcodeTable(eliminatedResult)
}

// intersect is a set operation implemented in a map
func intersect(a, b map[int]bool) map[int]bool {
	result := map[int]bool{}
	for k, v := range a {
		if v && b[k] {
			result[k] = true
		}
	}
	return result
}
