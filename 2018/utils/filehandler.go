package utils

import (
	"bufio"
	"log"
	"os"
	"path"
)

func check(e error) {
	if e != nil {
		log.Fatal(e)
	}
}

// LoadInput will the input file for the actual day
func LoadInput(project string) []string {
	var result = make([]string, 0)
	cwd, err := os.Getwd()
	check(err)
	fileToOpen := path.Join(cwd, project, "input.txt")
	file, err := os.Open(fileToOpen)
	check(err)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		result = append(result, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return result
}
