package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{
			Inp: []string{"Before: [3, 2, 1, 1]", "9 2 1 2", "After:  [3, 2, 2, 1]"},
			Exp: 1,
		},
	}

	for index, testcase := range data {
		result := ChronalClassification(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
