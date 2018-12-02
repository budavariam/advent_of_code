package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestProvided(t *testing.T) {
	data := []utils.Testcase{
		{Inp: []string{"abcdef"}, Exp: 0},
		{Inp: []string{"bababc"}, Exp: 1},
		{Inp: []string{"abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"}, Exp: 12},
	}

	for index, testcase := range data {
		result := MultiplyCountedwords(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
		}
	}
}
