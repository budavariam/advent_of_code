package main

import (
	"fmt"
	"sort"
)

type obstackles map[point]bool

type unitContainer struct {
	maxWidth  int
	maxHeight int
	counter
	unitList
	unitsByCoordinate map[point]*unit
	unitsByID         map[int]*unit
}

// add adds a new unit to the map
func (uc *unitContainer) add(newUnit unit) {
	uc.counter.increaseCounter(newUnit.spec)
	uc.unitsByID[newUnit.id] = &newUnit
	uc.unitsByCoordinate[newUnit.pos] = &newUnit
	uc.unitList = append(uc.unitList, &newUnit)
}

// sumHitPoints calculates the summary of hit points of all remaining units
func (uc *unitContainer) sumHitPoints() int {
	sum := 0
	for _, u := range uc.unitsByCoordinate {
		sum += u.hp
	}
	return sum
}

// filterAliveUnitList removes the dead units from the list, and reorders it by reading order
func (uc *unitContainer) filterAliveUnitList() unitList {
	result := make(unitList, 0)
	for _, u := range uc.unitList {
		if u.alive {
			result = append(result, u)
		}
	}
	sort.Sort(result)
	uc.unitList = result
	return result
}

// attack the selected unit decreases it's enemy's health by its attack point
func (uc *unitContainer) attack(currentUnit unit, otherUnitID int) {
	otherUnit := uc.unitsByID[otherUnitID]
	otherUnit.hp -= currentUnit.ap

	if otherUnit.hp <= 0 {
		uc.counter.decreaseCounter(otherUnit.spec)
		otherUnit.alive = false
		delete(uc.unitsByCoordinate, otherUnit.pos)
		uc.filterAliveUnitList()
	} else {
		uc.unitsByCoordinate[otherUnit.pos] = otherUnit
	}
}

// move changes the position of the selected unit to the destination point
func (uc *unitContainer) move(currentUnit *unit, nextStep point) {
	delete(uc.unitsByCoordinate, currentUnit.pos)
	currentUnit.pos = nextStep
	uc.unitsByCoordinate[nextStep] = currentUnit
}

// selectClosestUnit gets the nearest and weakes enemy, in case of a tie, it gets the first in reading order
func (uc *unitContainer) selectClosestUnit(currentUnit unit) unit {
	var otherUnit *unit
	minHealth := 201
	for _, diff := range directions {
		nextPos := diff.add(currentUnit.pos)
		if u, ok := uc.unitsByCoordinate[nextPos]; ok && u.alive && ((currentUnit.spec == goblin && u.spec == elf) || (currentUnit.spec == elf && u.spec == goblin)) && u.hp < minHealth {
			otherUnit = u
			minHealth = u.hp
		}
	}
	return *otherUnit
}

// findShortestDistance calculates the distances to all empty spots near enemies, and returns the distance and the first step towards that goal
func (uc *unitContainer) findShortestDistance(currentUnit unit, obst obstackles) (int, point) {
	spots := uc.getEmptySpots(currentUnit, obst)
	queue := make(distanceDataList, 0)
	queue = append(queue, distanceData{
		point:      currentUnit.pos,
		distance:   0,
		startPoint: currentUnit.pos,
		directions: make([]int, 0),
	})
	visited := make(map[point]bool)

	results := make(pathNodeList, 0)
	for len(queue) > 0 {
		actual := queue[0]
		queue = queue[1:]
		if visited[actual.point] {
			continue
		}
		visited[actual.point] = true

		if _, ok := spots[actual.point]; ok {
			if actual.distance > 0 {
				results = append(results, pathNode{
					step:     actual.distance,
					nextStep: currentUnit.pos.add(directions[actual.directions[0]]),
					goal:     actual.point,
				})
			} else {
				results = append(results, pathNode{
					step:     0,
					nextStep: actual.point,
					goal:     actual.point,
				})
			}
		}
		for directionIndex, diff := range directions {
			nextPos := actual.point.add(diff)
			_, hasUnitThere := uc.unitsByCoordinate[nextPos]
			if !obst[nextPos] &&
				!visited[nextPos] &&
				!hasUnitThere && nextPos.x >= 0 &&
				nextPos.y >= 0 &&
				nextPos.x < uc.maxWidth &&
				nextPos.y < uc.maxHeight {
				queue = append(queue, distanceData{
					point:      nextPos,
					distance:   actual.distance + 1,
					startPoint: actual.startPoint,
					directions: append(actual.directions, directionIndex),
				})
			}
		}
	}
	if len(results) == 0 {
		return -1, currentUnit.pos
	}
	sort.Sort(results)
	return results[0].step, results[0].nextStep
}

// getEmptySpots caclulates all places which are near enemies and not occupied
func (uc *unitContainer) getEmptySpots(currentUnit unit, obst obstackles) map[point]unitList {
	emptySpots := make(map[point]unitList)
	enemyRace := currentUnit.getEnemy()
	currentPos := currentUnit.pos

	for _, u := range uc.unitList {
		if u.spec == enemyRace {
			for _, diff := range directions {
				nextPos := u.pos.add(diff)
				_, hasUnitThere := uc.unitsByCoordinate[nextPos]
				_, notEmptySpot := emptySpots[nextPos]
				if nextPos.x >= 0 &&
					nextPos.y >= 0 &&
					nextPos.x < uc.maxWidth &&
					nextPos.y < uc.maxHeight &&
					!obst[nextPos] &&
					!hasUnitThere {
					emptySpots[nextPos] = append(emptySpots[nextPos], u)
				} else if currentPos == nextPos &&
					!notEmptySpot {
					// can attack
					emptySpots[nextPos] = append(emptySpots[nextPos], u)
				}
			}
		}
	}
	return emptySpots
}

// printUnits prints all units for debug purposes
func (uc *unitContainer) printUnits() {
	for _, u := range uc.unitList {
		fmt.Println(u.id, u.pos, u.hp)
	}
}
