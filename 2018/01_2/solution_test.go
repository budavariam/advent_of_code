package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{"+1", "-1"}, Exp: 0},
		{Inp: []string{"+3", "+3", "+4", "-2", "-4"}, Exp: 10},
		{Inp: []string{"-6", "+3", "+8", "+5", "-6"}, Exp: 5},
		{Inp: []string{"+7", "+7", "-2", "-7", "-4"}, Exp: 14},
	}

	for index, testcase := range data {
		result := ReachTwiceFirst(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
