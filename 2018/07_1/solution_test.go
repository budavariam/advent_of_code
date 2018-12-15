package main

import (
	"advent_of_code/2018/utils"
	"testing"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseStr{
		{Inp: []string{
			"Step C must be finished before step A can begin.",
			"Step C must be finished before step F can begin.",
			"Step A must be finished before step B can begin.",
			"Step A must be finished before step D can begin.",
			"Step B must be finished before step E can begin.",
			"Step D must be finished before step E can begin.",
			"Step F must be finished before step E can begin.",
		}, Exp: "CABDFE"},
	}

	for index, testcase := range data {
		result := TopologicalSort(testcase.Inp)
		if result != testcase.Exp {
			t.Errorf("%dth test was incorrect, got: %s, expected: %s.", index, result, testcase.Exp)
		}
	}
}
