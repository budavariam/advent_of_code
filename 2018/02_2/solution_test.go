package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseStr{
		{Inp: []string{"abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"}, Exp: "fgij"},
		{Inp: []string{"abcdde", "dfghjk", "dkghjk", "avcbde"}, Exp: "dghjk"},
	}

	for index, testcase := range data {
		result := GetClosestBoxes(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %s, expected: %s.", index, result, testcase.Exp)
		}
	}
}
