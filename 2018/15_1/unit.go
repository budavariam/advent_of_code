package main

type unit struct {
	id    int
	hp    int
	ap    int
	pos   point
	spec  int
	alive bool
}

type unitList []*unit

// getEnemy gets the enemy race identifier
func (u unit) getEnemy() int {
	if u.spec == elf {
		return goblin
	}
	return elf
}

// Sort units
func (u unitList) Len() int {
	return len(u)
}
func (u unitList) Less(i, j int) bool {
	return u[i].pos.lessThan(u[j].pos)
}
func (u unitList) Swap(i, j int) {
	u[j], u[i] = u[i], u[j]
}
