package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseStr{
		{Inp: []string{
			"|",
			"v",
			"|",
			"|",
			"|",
			"^",
			"|",
		}, Exp: "0,3"},
		{Inp: []string{
			"/->-\\        ",
			"|   |  /----\\",
			"| /-+--+-\\  |",
			"| | |  | v  |",
			"\\-+-/  \\-+--/",
			"  \\------/   ",
		}, Exp: "7,3"},
	}

	for index, testcase := range data {
		result := FirstCrashLocation(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %s, expected: %s.", index, result, testcase.Exp)
		}
	}
}
