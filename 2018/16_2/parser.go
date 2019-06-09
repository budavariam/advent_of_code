package main

// ParseData loads the data from the input
func ParseData(raw []string) ([]Observation, []Instruction) {
	observations, observationEndLine := parseObservations(raw)
	instructions := parseInstructions(raw[observationEndLine:])
	return observations, instructions
}

func parseObservations(data []string) ([]Observation, int) {
	length := len(data)
	result := []Observation{}
	rawIndex := 0
	for r := 0; rawIndex < length; rawIndex, r = rawIndex+4, r+1 {
		if data[rawIndex] == "" {
			rawIndex += 2 // step 2 more to get to the start of the instructions
			break         // the end of the observations is marked with a blank line
		}
		obs := Observation{}
		obs.init(data[rawIndex : rawIndex+3])
		result = append(result, obs)
	}
	return result, rawIndex
}

func parseInstructions(data []string) []Instruction {
	result := make([]Instruction, len(data))
	for lineNumber, rawInstruction := range data {
		result[lineNumber] = Instruction{}.init(rawInstruction)
	}
	return result
}
