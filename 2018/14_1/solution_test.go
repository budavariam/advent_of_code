package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseStr{
		{Inp: []string{"9"}, Exp: "5158916779"},
		{Inp: []string{"5"}, Exp: "0124515891"},
		{Inp: []string{"18"}, Exp: "9251071085"},
		{Inp: []string{"2018"}, Exp: "5941429882"},
	}

	for index, testcase := range data {
		result := TenRecipeScores(testcase.Inp[0])
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %s, expected: %s.", index, result, testcase.Exp)
		}
	}
}
