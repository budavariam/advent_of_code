package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{"1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"}, Exp: 16},
	}

	for index, testcase := range data {
		result := NearManyCoordinates(testcase.Inp, 32)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
