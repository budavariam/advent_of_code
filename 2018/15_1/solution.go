package main

import (
	"fmt"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("15_1")
	result := CombatOutcome(data)
	fmt.Println(result)
}

// CombatOutcome gets the outcome of the combat
func CombatOutcome(data []string) int {
	obst, units := parseMap(data)
	round := 0
	for units.counter.hasBothKind() {
		// fmt.Printf("Round %d\r\n", round)
		fullRound := true
		for _, currentUnit := range units.filterAliveUnitList() {
			if !units.counter.hasBothKind() {
				fullRound = false
			}
			if currentUnit.alive {
				plannedDistance, nextStep := units.findShortestDistance(*currentUnit, obst)
				if plannedDistance > 0 {
					units.move(currentUnit, nextStep)
					plannedDistance--
				}
				if plannedDistance == 0 {
					otherUnit := units.selectClosestUnit(*currentUnit)
					units.attack(*currentUnit, otherUnit.id)
				} else {
				}
			}
		}
		// printMap(data, units.unitList)
		// units.printUnits()
		if fullRound {
			round++
		}
	}
	remainingHitPoints := units.sumHitPoints()
	// fmt.Println(remainingHitPoints, round, remainingHitPoints*round)
	return remainingHitPoints * round
}

// parseMap processes the raw data
func parseMap(data []string) (obstackles, unitContainer) {
	obst := make(obstackles)
	units := unitContainer{
		counter:           counter{elf: 0, goblin: 0},
		maxWidth:          len(data[0]),
		maxHeight:         len(data),
		unitList:          make([]*unit, 0),
		unitsByCoordinate: make(map[point]*unit),
		unitsByID:         make(map[int]*unit),
	}
	id := 0
	for y, line := range data {
		for x, elem := range line {
			pos := point{x: x, y: y}
			switch elem {
			case '#':
				obst[pos] = true
			case 'G':
				id++
				unit := unit{hp: 200, ap: 3, pos: pos, spec: goblin, id: id, alive: true}
				units.add(unit)
			case 'E':
				id++
				unit := unit{hp: 200, ap: 3, pos: pos, spec: elf, id: id, alive: true}
				units.add(unit)
			}
		}
	}
	return obst, units
}
