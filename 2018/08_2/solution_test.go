package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{
			"2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2",
		}, Exp: 66},
	}

	for index, testcase := range data {
		result := RootValue(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
