package main

import (
	"testing"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func TestProvided(t *testing.T) {
	data := []utils.TestcaseNum{
		{Inp: []string{
			"#######",
			"#.G...#",
			"#...EG#",
			"#.#.#G#",
			"#..G#E#",
			"#.....#",
			"#######",
		}, Exp: 4988},

		{Inp: []string{
			"#######",
			"#E..EG#",
			"#.#G.E#",
			"#E.##E#",
			"#G..#.#",
			"#..E#.#",
			"#######",
		}, Exp: 31284},
		{Inp: []string{
			"#######",
			"#E.G#.#",
			"#.#G..#",
			"#G.#.G#",
			"#G..#.#",
			"#...E.#",
			"#######",
		}, Exp: 3478},
		{Inp: []string{
			"#######",
			"#.E...#",
			"#.#..G#",
			"#.###.#",
			"#E#G#G#",
			"#...#G#",
			"#######",
		}, Exp: 6474},
		{Inp: []string{
			"#########",
			"#G......#",
			"#.E.#...#",
			"#..##..G#",
			"#...##..#",
			"#...#...#",
			"#.G...G.#",
			"#.....G.#",
			"#########",
		}, Exp: 1140},
	}

	for index, testcase := range data {
		if 0 == 0 {
			result := CombatOutcomeNoLossElves(testcase.Inp)
			if result != testcase.Exp {
				t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
			}
		}
	}
}
