package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{
			Inp: []string{
				"pos=<0,0,0>, r=4",
				"pos=<1,0,0>, r=1",
				"pos=<4,0,0>, r=3",
				"pos=<0,2,0>, r=1",
				"pos=<0,5,0>, r=3",
				"pos=<0,0,3>, r=1",
				"pos=<1,1,1>, r=1",
				"pos=<1,1,2>, r=1",
				"pos=<1,3,1>, r=1",
			},
			Exp: 7},
	}

	for index, testcase := range data {
		result := EET(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
