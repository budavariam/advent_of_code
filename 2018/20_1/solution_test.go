package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{"^ENWWW(NEEE|SSE(EE|N))$"}, Exp: 10},
		{Inp: []string{"^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"}, Exp: 18},
		{Inp: []string{"^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"}, Exp: 23},
		{Inp: []string{"^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"}, Exp: 31},
	}

	for index, testcase := range data {
		result := RegularMap(testcase.Inp[0])
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
