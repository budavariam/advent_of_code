package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{
			"x=498, y=3..7",
			"x=506, y=2..7",
			"x=501, y=4..5",
			"x=503, y=4..5",
			"y=5, x=501..503",
			"y=8, x=498..506",
		}, Exp: 45},
		{Inp: []string{
			"x=495, y=2..7",
			"y=7, x=495..501",
			"x=501, y=3..7",
			"x=498, y=2..4",
			"x=506, y=1..2",
			"x=498, y=10..13",
			"x=504, y=10..13",
			"y=13, x=498..504",
		}, Exp: 57},
		{Inp: []string{
			"y=2, x=499..501",
			"x=499, y=5..6",
			"x=504, y=5..6",
			"y=6, x=500..503",
		}, Exp: 20},
		{Inp: []string{
			"y=7, x=499..501",
			"y=10, x=499..501",
			"x=499, y=7..10",
			"x=501, y=7..10",
			"x=493, y=2..15",
			"x=504, y=2..15",
			"y=15, x=493..504",
		}, Exp: 146},
	}

	for index, testcase := range data {
		result := ReservoirResearch(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
