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

func parseObservations(data []string) []Observation {
	length := len(data)
	result := []Observation{}
	for i, r := 0, 0; i < length; i, r = i+4, r+1 {
		if data[i] == "" {
			break // the end of the observations is marked with a blank line
		}
		obs := Observation{}
		obs.init(data[i : i+3])
		result = append(result, obs)
	}
	return result
}

func calcPossibilities(obs Observation) int {
	possibilities := map[string]func(i Instruction) Device{
		"addr": obs.before.addr,
		"addi": obs.before.addi,
		"mulr": obs.before.mulr,
		"muli": obs.before.muli,
		"banr": obs.before.banr,
		"bani": obs.before.bani,
		"borr": obs.before.borr,
		"bori": obs.before.bori,
		"setr": obs.before.setr,
		"seti": obs.before.seti,
		"gtir": obs.before.gtir,
		"gtri": obs.before.gtri,
		"gtrr": obs.before.gtrr,
		"eqir": obs.before.eqir,
		"eqri": obs.before.eqri,
		"eqrr": obs.before.eqrr,
	}
	count := 0
	for _, evaluator := range possibilities {
		res := evaluator(obs.instr)
		if res.isEqual(obs.after) {
			count++
		}
	}
	return count
}
