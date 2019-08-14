package main

type regionType byte

const (
	typeRocky regionType = iota
	typeWet
	typeNarrow
)

func (r regionType) print() string {
	switch r {
	case typeNarrow:
		return "narrow"
	case typeRocky:
		return "rocky"
	case typeWet:
		return "wet"
	default:
		return ""
	}
}
