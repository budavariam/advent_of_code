package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{"10 players; last marble is worth 1618 points"}, Exp: 8317},
		{Inp: []string{"13 players; last marble is worth 7999 points"}, Exp: 146373},
		{Inp: []string{"17 players; last marble is worth 1104 points"}, Exp: 2764},
		{Inp: []string{"21 players; last marble is worth 6111 points"}, Exp: 54718},
		{Inp: []string{"30 players; last marble is worth 5807 points"}, Exp: 37305},
	}

	for index, testcase := range data {
		result := WinnersScore(testcase.Inp[0])
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
