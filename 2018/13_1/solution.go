package main

import (
	"advent_of_code/2018/utils"
	"container/heap"
	"fmt"
)

func main() {
	data := utils.LoadInput("13_1/input.txt")
	result := FirstCrashLocation(data)
	fmt.Println(result)
}

//FirstCrashLocation simulates the ride and gets the location of the first crash
func FirstCrashLocation(input []string) string {
	//fmt.Println("***")
	tracks, carts, cartPositions := parseMap(input)
	crashes := []string{}
	for len(crashes) == 0 {
		carts, crashes, cartPositions = tick(tracks, carts, cartPositions)
	}
	return crashes[0]
}

// Cart represents a cart in the map
type Cart struct {
	id                int
	posX              int
	posY              int
	direction         int
	nextTurnDirection int
}

//Track represents a track in the map
type Track struct {
	posX      int
	posY      int
	tracktype int
}

const (
	north = iota
	east  = iota
	south = iota
	west  = iota
)

const (
	horizontal = iota
	vertical   = iota
	slash      = iota
	backslash  = iota
	crossing   = iota
)

const (
	left     = iota
	straight = iota
	right    = iota
)

func tick(tracks map[string]*Track, carts *Priority, cartPositions map[string]bool) (*Priority, []string, map[string]bool) {
	nextCarts := initCarts(0)
	crashes := []string{}
	for carts.Len() > 0 {
		cart := carts.Pop().(*Item).value
		prevPos, nextPos, cart := cart.move(tracks)
		//fmt.Println("Move cart: ", cart.id, prevPos, nextPos)
		if cartPositions[nextPos] {
			crashes = append(crashes, nextPos)
		}
		delete(cartPositions, prevPos)
		cartPositions[nextPos] = true
		nextCarts.Push(&Item{value: cart})
	}
	heap.Init(nextCarts)
	return nextCarts, crashes, cartPositions
}

func (c Cart) coords() string {
	return fmt.Sprintf("%d,%d", c.posX, c.posY)
}
func (t Track) coords() string {
	return fmt.Sprintf("%d,%d", t.posX, t.posY)
}

func (c *Cart) move(tracks map[string]*Track) (string, string, *Cart) {
	prevPos := c.coords()
	var nextPos string
	if currentTrack, ok := tracks[prevPos]; ok {
		nextPos = currentTrack.move(c)
	} else {
		panic(fmt.Sprintf("No such position: %s", prevPos))
	}
	return prevPos, nextPos, c
}

func (t Track) move(c *Cart) string {
	switch t.tracktype {
	// case horizontal:
	// case vertical:
	case slash:
		switch c.direction {
		case north:
			c.direction = east
		case east:
			c.direction = north
		case south:
			c.direction = west
		case west:
			c.direction = south
		}
	case backslash:
		switch c.direction {
		case north:
			c.direction = west
		case east:
			c.direction = south
		case south:
			c.direction = east
		case west:
			c.direction = north
		}
	case crossing:
		switch c.nextTurnDirection {
		case left:
			c.direction = (c.direction + 3) % 4
		case right:
			c.direction = (c.direction + 1) % 4
			// case straight:
		}
		c.nextTurnDirection = (c.nextTurnDirection + 1) % 3
	}
	c.reposition(c.direction)
	return c.coords()
}

func (c *Cart) reposition(direction int) {
	switch direction {
	case north:
		c.posY--
	case east:
		c.posX++
	case south:
		c.posY++
	case west:
		c.posX--
	}
}

func parseMap(data []string) (map[string]*Track, *Priority, map[string]bool) {
	carts := initCarts(0)
	tracks := map[string]*Track{}
	cartPositions := map[string]bool{}
	cartID := 0
	for y, line := range data {
		for x, elem := range line {
			if elem != ' ' {
				horizontalCart := elem == '<' || elem == '>'
				verticalCart := elem == 'v' || elem == '^'
				track := &Track{posX: x, posY: y, tracktype: -1}
				if horizontalCart || verticalCart {
					cart := &Cart{posX: x, posY: y, direction: -1, id: cartID}
					cartID++
					switch elem {
					case '<':
						cart.direction = west
					case '>':
						cart.direction = east
					case 'v':
						cart.direction = south
					case '^':
						cart.direction = north
					}
					cartPositions[cart.coords()] = true
					carts.Push(&Item{value: cart})
					if horizontalCart {
						track.tracktype = horizontal
					} else {
						track.tracktype = vertical
					}
				} else {
					switch elem {
					case '+':
						track.tracktype = crossing
					case '/':
						track.tracktype = slash
					case '\\':
						track.tracktype = backslash
					case '-':
						track.tracktype = horizontal
					case '|':
						track.tracktype = vertical
					}
				}
				tracks[track.coords()] = track
			}
		}
	}
	heap.Init(carts)
	return tracks, carts, cartPositions
}

func initCarts(length int) *Priority {
	pq := make(Priority, length)
	heap.Init(&pq)
	return &pq
}
