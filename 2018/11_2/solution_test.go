package main

import (
	"testing"
)

func TestLocationOfMaxPowerLevelsAndGridSize(t *testing.T) {
	data := []struct {
		sn       string
		expPower int
		expSize  int
		expX     int
		expY     int
	}{
		{"18", 113, 16, 90, 269},
		{"42", 119, 12, 232, 251},
	}

	for index, testcase := range data {
		topleftX, topleftY, size, powerLevel := GetLargestPowerLevelOfAnySize(testcase.sn, 300, 300)
		if topleftX != testcase.expX || topleftY != testcase.expY {
			t.Errorf("%dth test was incorrect, got: %d,%d,%d (%d), expected: %d,%d,%d.", index, topleftX, topleftY, size, powerLevel, testcase.expX, testcase.expY, testcase.expSize)
		}
	}
}
