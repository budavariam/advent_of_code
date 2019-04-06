package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{"aA"}, Exp: 0},
		{Inp: []string{"abBA"}, Exp: 0},
		{Inp: []string{"abAB"}, Exp: 4},
		{Inp: []string{"aabAAB"}, Exp: 6},
		{Inp: []string{"dabAcCaCBAcCcaDA"}, Exp: 10},
	}

	for index, testcase := range data {
		result := LengthAfterReactions(testcase.Inp[0])
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
