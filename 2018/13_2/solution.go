package main

import (
	"fmt"
	"sort"

	"github.com/budavariam/advent_of_code/2018/utils"
)

func main() {
	data := utils.LoadInput("13_2")
	result := LastCartLocation(data)
	fmt.Println(result)
}

//LastCartLocation simulates the ride and gets the location of the last standing cart
func LastCartLocation(input []string) string {
	tracks, carts, cartPositions := parseMap(input)
	for carts.Len() > 1 {
		carts, cartPositions = tick(tracks, carts, cartPositions)
	}
	return carts[0].coords()
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
type Track int

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

func tick(tracks map[string]Track, carts CartContainer, cartPositions map[string]*Cart) (CartContainer, map[string]*Cart) {
	crashedIDs := map[int]bool{}
	for len(carts) > 0 {
		cart := carts[0]
		carts = carts[1:]
		prevPos, nextPos, cart := cart.move(tracks)
		delete(cartPositions, prevPos)
		//fmt.Println("Move cart: ", cart.id, prevPos, nextPos)
		if otherCart, currentCrash := cartPositions[nextPos]; currentCrash || crashedIDs[cart.id] {
			//fmt.Printf("Cart %d crashed. Remove it.\n", cart.id)
			if currentCrash {
				//fmt.Printf("Cart %d and %d have crashed. Remove them.\n", cart.id, otherCart.id)
				crashedIDs[otherCart.id] = true
				delete(cartPositions, nextPos)
			}
		} else {
			// add the cart to the intact ones if it didn't crash now, or another one haven't hit it.
			cartPositions[nextPos] = cart
		}
	}
	nextCarts := make(CartContainer, len(cartPositions))
	i := 0
	for _, cart := range cartPositions {
		nextCarts[i] = cart
		i++
	}
	sort.Sort(nextCarts)
	return nextCarts, cartPositions
}

func (c Cart) coords() string {
	return fmt.Sprintf("%d,%d", c.posX, c.posY)
}

func (c *Cart) move(tracks map[string]Track) (string, string, *Cart) {
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
	switch t {
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

func parseMap(data []string) (map[string]Track, CartContainer, map[string]*Cart) {
	tracks := map[string]Track{}
	cartPositions := map[string]*Cart{}
	carts := make(CartContainer, 0)
	cartID := 0
	for y, line := range data {
		for x, elem := range line {
			if elem != ' ' {
				horizontalCart := elem == '<' || elem == '>'
				verticalCart := elem == 'v' || elem == '^'
				track := Track(-1)
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
					cartPositions[cart.coords()] = cart
					carts = append(carts, cart)
					if horizontalCart {
						track = horizontal
					} else {
						track = vertical
					}
				} else {
					switch elem {
					case '+':
						track = crossing
					case '/':
						track = slash
					case '\\':
						track = backslash
					case '-':
						track = horizontal
					case '|':
						track = vertical
					}
				}
				tracks[fmt.Sprintf("%d,%d", x, y)] = track
			}
		}
	}
	return tracks, carts, cartPositions
}
