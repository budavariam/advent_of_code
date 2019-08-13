package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{
			Inp: []string{
				"depth: 510",
				"target: 10,10"},
			Exp: 114},
	}

	for index, testcase := range data {
		result := ModeMaze(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
