package main

type counter struct {
	elf    int
	goblin int
}

// increaseCounter marks one less item from a species
func (c *counter) decreaseCounter(spec int) {
	if spec == goblin {
		c.goblin--
	} else {
		c.elf--
	}
}

// increaseCounter marks one more item from a species
func (c *counter) increaseCounter(spec int) {
	if spec == goblin {
		c.goblin++
	} else {
		c.elf++
	}
}

// hasBothKind checks if all species has at least one unit
func (c *counter) hasBothKind() bool {
	return c.goblin > 0 && c.elf > 0
}
