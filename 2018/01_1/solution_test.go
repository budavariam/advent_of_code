package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestSum(t *testing.T) {
	data := []utils.Testcase{
		{Inp: []string{"1"}, Exp: 1},
		{Inp: []string{"+1", "+1", "+1"}, Exp: 3},
		{Inp: []string{"+1", "+1", "-2"}, Exp: 0},
		{Inp: []string{"-1", "-2", "-3"}, Exp: -6},
	}

	for index, testcase := range data {
		total := Sum(testcase.Inp)
		if total != testcase.Exp {
			t.Errorf("%dth sum was incorrect, got: %d, want: %d.", index, total, testcase.Exp)
		}
	}
}
