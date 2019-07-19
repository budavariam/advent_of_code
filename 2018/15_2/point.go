package main

type point struct {
	x int
	y int
}

type pointList []point

// lessThan compares 2 points
func (p point) lessThan(other point) bool {
	if p.y == other.y {
		return p.x < other.x
	}
	return p.y < other.y
}

// equal compares 2 points
func (p point) equal(other point) bool {
	return p.y == other.y && p.x == other.x
}

// add sums 2 points
func (p point) add(other point) point {
	return point{x: p.x + other.x, y: p.y + other.y}
}

// Sort points
func (p pointList) Len() int {
	return len(p)
}

func (p pointList) Less(i, j int) bool {
	return p[i].lessThan(p[j])
}

func (p pointList) Swap(i, j int) {
	p[j], p[i] = p[i], p[j]
}
