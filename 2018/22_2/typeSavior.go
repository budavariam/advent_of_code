package main

import "math"

type savior struct {
	currentItem  itemType
	currentCoord coord
	timeTaken    int
}

func (s *savior) sameState(other savior) bool {
	return s.currentItem == other.currentItem && s.currentCoord == other.currentCoord
}

var allowedTools = map[regionType]map[itemType]bool{
	typeRocky:  map[itemType]bool{climbingGear: true, torch: true},
	typeWet:    map[itemType]bool{climbingGear: true, neither: true},
	typeNarrow: map[itemType]bool{torch: true, neither: true},
}

func (s *savior) newState(nextCoord coord, c *cartograph) []savior {
	nextMoves := []savior{}

	currentRegionType := c.carta[s.currentCoord].regionType
	nextRegionType := c.carta[nextCoord].regionType

	for item := range allowedTools[currentRegionType] {
		if item != s.currentItem {
			nextMoves = append(nextMoves, savior{
				currentItem:  item,
				currentCoord: s.currentCoord,
				timeTaken:    s.timeTaken + 7,
			})
		}
		if item == s.currentItem && allowedTools[nextRegionType][item] {
			nextMoves = append(nextMoves, savior{
				currentItem:  s.currentItem,
				currentCoord: nextCoord,
				timeTaken:    s.timeTaken + 1,
			})
		}
	}

	return nextMoves
}

func (s savior) FindQuickestWay(c *cartograph) int {
	finalPos := savior{currentItem: torch, currentCoord: c.target}
	minimalReachTime := int(math.MaxUint64 >> 1)

	type visitedRegion struct {
		pos  coord
		item itemType
	}
	visited := map[visitedRegion]int{}

	queue := []savior{s}
	for len(queue) > 0 {
		currentPos := queue[0]
		queue = queue[1:]
		regionInfo := visitedRegion{pos: currentPos.currentCoord, item: currentPos.currentItem}
		if val, ok := visited[regionInfo]; ok && val <= currentPos.timeTaken {
			continue
		} else {
			visited[regionInfo] = currentPos.timeTaken
		}

		//reached the end
		if finalPos.sameState(currentPos) {
			if currentPos.timeTaken < minimalReachTime {
				// it has reached the end in a better time than the others
				minimalReachTime = currentPos.timeTaken
			}
			continue
		}
		if currentPos.timeTaken > minimalReachTime {
			// there is no chance it will be faster
			continue
		}

		// move forward or change gear
		for _, dir := range directions {
			nextCoord := currentPos.currentCoord.add(dir)
			if _, ok := c.carta[nextCoord]; ok {
				queue = append(queue, currentPos.newState(nextCoord, c)...)
			}

		}
	}
	return minimalReachTime
}
