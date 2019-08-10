package main

import "math"

type distanceMap map[coord]int

// get returns infinite in case it does not find the value
func (d distanceMap) get(c coord) int {
	if val, ok := d[c]; ok {
		return val
	}
	return int(math.MaxUint64 >> 1)
}
