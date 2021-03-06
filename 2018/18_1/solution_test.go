package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{
			Inp: []string{
				".#.#...|#.",
				".....#|##|",
				".|..|...#.",
				"..|#.....#",
				"#.#|||#|#|",
				"...#.||...",
				".|....|...",
				"||...#|.#|",
				"|.||||..|.",
				"...#.|..|."},
			Exp: 1147},
	}

	for index, testcase := range data {
		result := SimulateLumberChange(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
