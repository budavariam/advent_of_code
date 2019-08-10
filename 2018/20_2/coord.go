package main

type coord [2]int

func newCoord(y, x int) coord {
	return [2]int{y, x}
}

func (c coord) add(o coord) coord {
	return newCoord(c[0]+o[0], c[1]+o[1])
}
