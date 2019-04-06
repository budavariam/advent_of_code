package main

import (
	"fmt"
	"regexp"
	"sort"
	"strconv"
	"time"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("04_1")
	result := ChooseGuardAndMinute(data)
	fmt.Println(result)
}

type logline struct {
	timestamp   time.Time
	minute      int
	guardPos    int
	guardID     int
	wakesUp     bool
	fallsAsleep bool
}

type fullLog []logline

func (p fullLog) Len() int {
	return len(p)
}

func (p fullLog) Less(i, j int) bool {
	return p[i].timestamp.Before(p[j].timestamp)
}

func (p fullLog) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func parseTextInput(data []string) (fullLog, map[int]bool) {
	result := make(fullLog, 0)
	guards := make(map[int]bool)
	currentGuard := -1
	for _, line := range data {
		regex := *regexp.MustCompile(`\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (?:Guard #(\d+)|(w)|(f))`)
		parsedData := regex.FindAllStringSubmatch(line, -1)
		year, _ := strconv.Atoi(parsedData[0][1])
		month, _ := strconv.Atoi(parsedData[0][2])
		day, _ := strconv.Atoi(parsedData[0][3])
		hour, _ := strconv.Atoi(parsedData[0][4])
		minute, _ := strconv.Atoi(parsedData[0][5])
		guardID, _ := strconv.Atoi(parsedData[0][6])
		if guardID > 0 {
			guards[guardID] = true
			currentGuard = guardID
		} else {
			// currently the guards are unordered, so only set the guardID where it is known.
			currentGuard = -1
		}
		wakesUp := false
		if parsedData[0][7] == "w" {
			wakesUp = true
		}
		fallsAsleep := false
		if parsedData[0][8] == "f" {
			fallsAsleep = true
		}
		newLogLine := logline{
			timestamp:   time.Date(year, time.Month(month), day, hour, minute, 0, 0, time.UTC),
			minute:      minute,
			guardID:     currentGuard,
			wakesUp:     wakesUp,
			fallsAsleep: fallsAsleep,
		}
		result = append(result, newLogLine)
	}
	sort.Sort(result)
	result = fillMissingGuardIDs(result)
	return result, guards
}

func buildTimeline(parsedLines fullLog, guards map[int]bool) int {
	timeline := make(map[int][]int, len(guards))
	for guardID := range guards {
		timeline[guardID] = make([]int, 60)
	}
	prevMinute := -1
	sleepMinute := make(map[int]int, len(guards))
	maxSleepTime := -1
	selectedGuard := -1
	for _, line := range parsedLines {
		if line.wakesUp {
			for setMinute := prevMinute; setMinute < line.minute; setMinute++ {
				timeline[line.guardID][setMinute]++
			}
			sleepMinute[line.guardID] += line.minute - prevMinute
			if sleepMinute[line.guardID] > maxSleepTime {
				maxSleepTime = sleepMinute[line.guardID]
				selectedGuard = line.guardID
			}
		}
		prevMinute = line.minute
	}
	maxMinute := findIndexOfLargestValueInList(timeline[selectedGuard])
	return maxMinute * selectedGuard
}

// ChooseGuardAndMinute returns the multiplication of the selected guard and the selected minute
func ChooseGuardAndMinute(data []string) int {
	parsedLines, guards := parseTextInput(data)
	result := buildTimeline(parsedLines, guards)
	return result
}

// fillMissingGuardIDs adds the guardID data to the ordered list
func fillMissingGuardIDs(result fullLog) fullLog {
	prevGuard := -1
	for index, line := range result {
		if line.guardID > -1 {
			prevGuard = line.guardID
		} else {
			result[index].guardID = prevGuard
		}
	}
	return result
}

// findIndexOfLargestValueInList returns the frst index of the largest value in the list
func findIndexOfLargestValueInList(data []int) int {
	maxValue := -1
	maxMinute := -1
	for minute, elem := range data {
		if elem > maxValue {
			maxValue = elem
			maxMinute = minute
		}
	}
	return maxMinute
}
