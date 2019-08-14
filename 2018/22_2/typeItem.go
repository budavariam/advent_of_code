package main

type itemType byte

const (
	neither itemType = iota
	climbingGear
	torch
)

func (i itemType) print() string {
	switch i {
	case neither:
		return "neither item"
	case climbingGear:
		return "climbing gear"
	case torch:
		return "torch"
	default:
		return ""
	}
}
