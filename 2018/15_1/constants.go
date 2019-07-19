package main

const (
	goblin = iota
	elf
)

var (
	directions = [4]point{
		point{x: 0, y: -1}, //up
		point{x: -1, y: 0}, //left
		point{x: 1, y: 0},  //right
		point{x: 0, y: 1},  //down
	}
)