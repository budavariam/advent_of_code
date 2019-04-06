package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{"10 players; last marble is worth 1618 points"}, Exp: 74765078},
		{Inp: []string{"13 players; last marble is worth 7999 points"}, Exp: 1406506154},
		{Inp: []string{"17 players; last marble is worth 1104 points"}, Exp: 20548882},
		{Inp: []string{"21 players; last marble is worth 6111 points"}, Exp: 507583214},
		{Inp: []string{"30 players; last marble is worth 5807 points"}, Exp: 320997431},
	}

	for index, testcase := range data {
		result := WinnersScore(testcase.Inp[0])
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
