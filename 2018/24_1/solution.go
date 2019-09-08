package main

import (
	"fmt"
	"regexp"
	"sort"
	"strconv"
	"strings"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	input := utils.LoadInput("24_1")
	result := ImmuneSystemSimulator(input)
	fmt.Println(result)
}

// ImmuneSystemSimulator simulates the special reindeer immune system
func ImmuneSystemSimulator(input []string) int {
	battle := parseInput(input)
	for !battle.isFightOver() {
		targets := battle.targetSelectionPhase()
		battle.attackPhase(targets)
	}
	return battle.countWinningArmyUnits()
}

func parseInput(input []string) battleGround {
	unitRegex := *regexp.MustCompile(`^(\d+)[a-z ]+(\d+)[a-z ]+(?:\(([^\)]*)\) )?[a-z ]+(\d+) (\w+)[a-z ]+(\d+)$`)
	teamRegex := *regexp.MustCompile(`^([a-zA-Z ]+):$`)
	currentTeamNr := -1
	units := unitContainer{}
	teams := teamList{}
	for lineNr, line := range input {
		if unitRegex.MatchString(line) {
			rawUnit := unitRegex.FindStringSubmatch(line)
			count, _ := strconv.Atoi(rawUnit[1])
			hp, _ := strconv.Atoi(rawUnit[2])
			immuneTo, weakTo := parseImmunesAndWeaknesses(rawUnit[3])
			ap, _ := strconv.Atoi(rawUnit[4])
			attackType := rawUnit[5]
			initiative, _ := strconv.Atoi(rawUnit[6])

			parsedUnit := unit{
				id:         lineNr,
				count:      count,
				hp:         hp,
				immuneTo:   immuneTo,
				weakTo:     weakTo,
				ap:         ap,
				attackType: attackType,
				initiative: initiative,
				team:       currentTeamNr,
			}
			parsedUnit.calcEffectivePower()
			units[lineNr] = &parsedUnit
			teams[currentTeamNr][lineNr] = &parsedUnit
		} else if teamRegex.MatchString(line) {
			currentTeamNr++
			teams = append(teams, make(unitContainer, 0))
		}
	}
	return battleGround{
		units: units,
		teams: teams,
	}
}

func parseImmunesAndWeaknesses(input string) (set, set) {
	immuneTo := set{}
	weakTo := set{}
	if input == "" {
		return immuneTo, weakTo
	}
	iwRegex := *regexp.MustCompile(`(immune|weak) to ([^;\)]+)`)
	rawData := iwRegex.FindAllStringSubmatch(input, -1)
	for _, matches := range rawData {
		iwType := matches[1]
		for _, iw := range strings.Split(matches[2], ", ") {
			if iwType == "immune" {
				immuneTo[iw] = true
			} else {
				weakTo[iw] = true
			}
		}
	}

	return immuneTo, weakTo
}

type unitContainer map[int]*unit
type teamList []unitContainer

type set map[string]bool

type unit struct {
	id             int
	count          int
	hp             int
	immuneTo       set
	weakTo         set
	ap             int
	attackType     string
	initiative     int
	team           int
	effectivePower int
}

func (u *unit) calcEffectivePower() {
	u.effectivePower = u.count * u.ap
}

func (u *unit) countDamage(enemy *unit) int {
	if _, has := enemy.immuneTo[u.attackType]; has {
		return 0
	} else if _, has := enemy.weakTo[u.attackType]; has {
		return 2 * u.effectivePower
	}
	return u.effectivePower
}

func (u *unit) takeDamage(dmg int) bool {
	killNrOfUnits := dmg / u.hp
	if killNrOfUnits >= u.count {
		u.count = 0
		return false
	}
	u.count -= killNrOfUnits
	u.calcEffectivePower()
	return true
}

func (u *unit) selectEnemy(enemies unitContainer, alreadySelected unitSet) *unit {
	selectedEnemy := &unit{}
	currentMaxDmg := 0
	for _, enemy := range enemies {
		if alreadySelected[enemy] {
			continue
		}
		dmg := u.countDamage(enemy)
		// dmg, effectivepw, initiative
		// fmt.Printf("#%d group #%d unit would deal defending group #%d unit %d damage\r\n", u.team, u.id, enemy.id, dmg)
		if (dmg > currentMaxDmg) ||
			(dmg == currentMaxDmg && enemy.effectivePower > selectedEnemy.effectivePower) ||
			(dmg == currentMaxDmg && enemy.effectivePower == selectedEnemy.effectivePower && enemy.initiative > selectedEnemy.initiative) {
			selectedEnemy = enemy
			currentMaxDmg = dmg
		}
	}
	if selectedEnemy.id == 0 {
		return nil
	}
	return selectedEnemy
}

type unitSet map[*unit]bool
type unitList []*unit

func (ddl unitList) Len() int {
	return len(ddl)
}

func (ddl unitList) Less(i, j int) bool {
	if ddl[i].effectivePower == ddl[j].effectivePower {
		return ddl[i].initiative > ddl[j].initiative
	}
	return ddl[i].effectivePower > ddl[j].effectivePower
}

func (ddl unitList) Swap(i, j int) {
	ddl[j], ddl[i] = ddl[i], ddl[j]
}

type unitListByInitiative []*unit

func (ddl unitListByInitiative) Len() int {
	return len(ddl)
}

func (ddl unitListByInitiative) Less(i, j int) bool {
	return ddl[i].initiative > ddl[j].initiative
}

func (ddl unitListByInitiative) Swap(i, j int) {
	ddl[j], ddl[i] = ddl[i], ddl[j]
}

type battleGround struct {
	teams teamList
	units unitContainer
}

func (bg *battleGround) isFightOver() bool {
	isOver := false
	for _, team := range bg.teams {
		if len(team) == 0 {
			isOver = true
			break
		}
	}
	return isOver
}

func (bg *battleGround) countWinningArmyUnits() int {
	result := 0
	for _, team := range bg.teams {
		for _, unit := range team {
			result += unit.count
		}
	}
	return result
}

type target struct {
	enemy *unit
}
type targetMapping map[*unit]target

func (bg *battleGround) targetSelectionPhase() targetMapping {
	// fmt.Println("Target selection phase")
	mapping := targetMapping{}
	selectorOrder := getUnitList(bg.units)
	sort.Sort(unitList(selectorOrder))
	alreadySelected := unitSet{}
	// for _, currentUnit := range selectorOrder {
	// 	fmt.Printf("Group %d contains %d units (%+v)\r\n", currentUnit.id, currentUnit.count, currentUnit)
	// }
	for _, currentUnit := range selectorOrder {
		selectedEnemy := currentUnit.selectEnemy(bg.teams[1-currentUnit.team], alreadySelected)
		if selectedEnemy != nil {
			mapping[currentUnit] = target{enemy: selectedEnemy}
			alreadySelected[selectedEnemy] = true
		}
	}

	return mapping
}

func getUnitList(units unitContainer) unitList {
	result := make(unitList, len(units))
	i := 0
	for _, u := range units {
		result[i] = u
		i++
	}
	return result
}

func (bg *battleGround) attackPhase(targets targetMapping) {
	// fmt.Println("Attack phase")
	units := getUnitList(bg.units)
	sort.Sort(unitListByInitiative(units))
	for _, attacker := range units {
		if tgt, has := targets[attacker]; has {
			damage := attacker.countDamage(tgt.enemy)
			// fmt.Printf("#%d group #%d unit attacks defending group #%d killing %d units\r\n", attacker.team, attacker.id, tgt.enemy.id, min(damage/tgt.enemy.hp, tgt.enemy.count))
			survived := tgt.enemy.takeDamage(damage)
			if !survived {
				delete(bg.teams[tgt.enemy.team], tgt.enemy.id)
				delete(bg.units, tgt.enemy.id)
				delete(targets, tgt.enemy)
			}
		}
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
