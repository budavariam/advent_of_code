package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{
			Inp: []string{
				"#ip 0",
				"seti 5 0 1",
				"seti 6 0 2",
				"addi 0 1 0",
				"addr 1 2 3",
				"setr 1 0 0",
				"seti 8 0 4",
				"seti 9 0 5"},
			Exp: 6},
	}

	for index, testcase := range data {
		result := GoWithTheFlow(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
