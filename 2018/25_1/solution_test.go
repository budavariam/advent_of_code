package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{
			Inp: []string{
				"0,0,0,0",
				"3,0,0,0",
				"0,3,0,0",
				"0,0,3,0",
				"0,0,0,3",
				"0,0,0,6",
				"9,0,0,0",
				"12,0,0,0",
			},
			Exp: 2},
		{
			Inp: []string{
				"-1,2,2,0",
				"0,0,2,-2",
				"0,0,0,-2",
				"-1,2,0,0",
				"-2,-2,-2,2",
				"3,0,2,-1",
				"-1,3,2,2",
				"-1,0,-1,0",
				"0,2,1,-2",
				"3,0,0,0",
			},
			Exp: 4},
		{
			Inp: []string{
				"1,-1,0,1",
				"2,0,-1,0",
				"3,2,-1,0",
				"0,0,3,1",
				"0,0,-1,-1",
				"2,3,-2,0",
				"-2,2,0,0",
				"2,-2,0,-1",
				"1,-1,0,-1",
				"3,2,0,2",
			},
			Exp: 3},
		{
			Inp: []string{
				"1,-1,-1,-2",
				"-2,-2,0,1",
				"0,2,1,3",
				"-2,3,-2,1",
				"0,2,3,-2",
				"-1,-1,1,-2",
				"0,-2,-1,0",
				"-2,2,3,-1",
				"1,2,2,0",
				"-1,-2,0,-2",
			},
			Exp: 8},
	}

	for index, testcase := range data {
		result := Constellations(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
