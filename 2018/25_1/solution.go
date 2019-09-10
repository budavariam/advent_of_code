package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	input := utils.LoadInput("25_1")
	result := Constellations(input)
	fmt.Println(result)
}

// Constellations simulates the special reindeer immune system
func Constellations(input []string) int {
	stars := parseInput(input)
	cons := spacetime{
		neighbours:         generateDifferences(),
		lastID:             len(stars),
		constellationCount: len(stars),
		visitedStars:       map[coord]*star{},
		constellations:     map[int][]*star{},
	}
	for i := range stars {
		cons.constellations[stars[i].constellation] = []*star{&stars[i]}
	}

	for i := range stars {
		cons.add(&stars[i])
	}
	return cons.constellationCount
}

func parseInput(input []string) []star {
	result := make([]star, len(input))
	for n, line := range input {
		rawCoords := strings.Split(line, ",")
		starLocation := coord{}
		for i, pos := range rawCoords {
			starLocation[i], _ = strconv.Atoi(pos)
		}
		result[n] = star{
			id:            n,
			location:      starLocation,
			constellation: n,
		}
	}
	return result
}

type coord [4]int

func (c coord) add(other coord) coord {
	return coord{
		c[0] + other[0],
		c[1] + other[1],
		c[2] + other[2],
		c[3] + other[3],
	}
}

type star struct {
	id            int
	location      coord
	constellation int
}
type spacetime struct {
	constellations     map[int][]*star
	visitedStars       map[coord]*star
	constellationCount int
	lastID             int
	neighbours         []coord
}

func (st *spacetime) add(newStar *star) {
	// check the surroundings for already visited stars
	neighboringConstellationIDs := map[int]bool{}
	for _, nearbyPos := range st.neighbours {
		newPos := newStar.location.add(nearbyPos)
		if otherStar, ok := st.visitedStars[newPos]; ok {
			neighboringConstellationIDs[otherStar.constellation] = true
		}
	}
	st.visitedStars[newStar.location] = newStar
	if len(neighboringConstellationIDs) > 0 {
		// if found then merge all of them into a new constellation
		newConstellationStars := []*star{newStar}
		st.constellationCount = st.constellationCount - len(neighboringConstellationIDs)
		for constID := range neighboringConstellationIDs {
			newConstellationStars = append(newConstellationStars, st.constellations[constID]...)
			delete(st.constellations, constID)
		}
		delete(st.constellations, newStar.constellation)
		st.lastID++
		for _, s := range newConstellationStars {
			s.constellation = st.lastID
		}
		st.constellations[st.lastID] = newConstellationStars
	}
}

func generateDifferences() []coord {
	result := []coord{}
	x, y, z, a := 0, 0, 0, 0
	for xNew := x - 3; xNew <= x+3; xNew++ {
		for yNew := y - 3; yNew <= y+3; yNew++ {
			for zNew := z - 3; zNew <= z+3; zNew++ {
				for aNew := a - 3; aNew <= a+3; aNew++ {
					if abs(xNew)+abs(yNew)+abs(zNew)+abs(aNew) <= 3 {
						result = append(result, coord{xNew, yNew, zNew, aNew})
					}
				}
			}
		}
	}
	return result
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
