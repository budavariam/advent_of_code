package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{"1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"}, Exp: 17},
	}

	for index, testcase := range data {
		result := GetMaximalInnerArea(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
