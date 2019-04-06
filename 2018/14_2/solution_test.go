package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseStr{
		{Inp: []string{"51589"}, Exp: "9"},
		{Inp: []string{"01245"}, Exp: "5"},
		{Inp: []string{"92510"}, Exp: "18"},
		{Inp: []string{"59414"}, Exp: "2018"},
	}

	for index, testcase := range data {
		result := RecipeCountBeforeValue(testcase.Inp[0])
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %s, expected: %s.", index, result, testcase.Exp)
		}
	}
}
