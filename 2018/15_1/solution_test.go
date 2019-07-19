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
		}, Exp: 27730},
		{Inp: []string{
			"#######",
			"#G..#E#",
			"#E#E.E#",
			"#G.##.#",
			"#...#E#",
			"#...E.#",
			"#######",
		}, Exp: 36334},
		{Inp: []string{
			"#######",
			"#E..EG#",
			"#.#G.E#",
			"#E.##E#",
			"#G..#.#",
			"#..E#.#",
			"#######",
		}, Exp: 39514},
		{Inp: []string{
			"#######",
			"#E.G#.#",
			"#.#G..#",
			"#G.#.G#",
			"#G..#.#",
			"#...E.#",
			"#######",
		}, Exp: 27755},
		{Inp: []string{
			"#######",
			"#.E...#",
			"#.#..G#",
			"#.###.#",
			"#E#G#G#",
			"#...#G#",
			"#######",
		}, Exp: 28944},
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
		}, Exp: 18740},
	}

	for index, testcase := range data {
		if 0 == 0 {
			result := CombatOutcome(testcase.Inp)
			if result != testcase.Exp {
				t.Errorf("%dth test was incorrect, got: %d, expected: %d.", index, result, testcase.Exp)
			}
		}
	}
}
