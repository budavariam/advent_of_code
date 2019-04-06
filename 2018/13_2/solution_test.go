package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseStr{
		{Inp: []string{
			"/>-<\\  ",
			"|   |  ",
			"| /<+-\\",
			"| | | v",
			"\\>+</ |",
			"  |   ^",
			"  \\<->/",
		}, Exp: "6,4"},
	}

	for index, testcase := range data {
		result := LastCartLocation(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %s, expected: %s.", index, result, testcase.Exp)
		}
	}
}
