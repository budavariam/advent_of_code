package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestPowerLevels(t *testing.T) {
	data := []struct {
		x          int
		y          int
		sn         int
		powerLevel int
	}{
		{3, 5, 8, 4},
		{122, 79, 57, -5},
		{217, 196, 39, 0},
		{101, 153, 71, 4},
	}

	for index, tdata := range data {
		result := CalculatePowerLevel(tdata.sn, tdata.y, tdata.x)
		if result != tdata.powerLevel {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, tdata.powerLevel)
		}
	}
}

func TestMaxPowerLevels(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{"18"}, Exp: 29},
		{Inp: []string{"42"}, Exp: 30},
	}

	for index, testcase := range data {
		result, _, _ := GetLargestPowerLevel(testcase.Inp[0], 300, 300)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}

func TestLocationOfMaxPowerLevels(t *testing.T) {
	data := []struct {
		sn   string
		expX int
		expY int
	}{
		{"18", 33, 45},
		{"42", 21, 61},
	}

	for index, testcase := range data {
		powerLevel, topleftX, topleftY := GetLargestPowerLevel(testcase.sn, 300, 300)
		if topleftX != testcase.expX || topleftY != testcase.expY {
			t.Errorf("%dth test was incorrect, got: %d,%d (%d), expected: %d,%d.", index, topleftX, topleftY, powerLevel, testcase.expX, testcase.expY)
		}
	}
}
