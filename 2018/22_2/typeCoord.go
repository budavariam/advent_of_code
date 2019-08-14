package main

type coord struct {
	X int
	Y int
}

func (c *coord) add(other coord) coord {
	return coord{X: c.X + other.X, Y: c.Y + other.Y}
}

var directions = []coord{
	coord{X: -1, Y: 0},
	coord{X: 0, Y: -1},
	coord{X: 1, Y: 0},
	coord{X: 0, Y: 1},
}
