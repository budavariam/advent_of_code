package main

// CartContainer contains carts in appropriate order
type CartContainer []*Cart

func (pq CartContainer) Len() int { return len(pq) }

func (pq CartContainer) Less(i, j int) bool {
	if pq[i].posY == pq[j].posY {
		return pq[i].posX < pq[j].posX
	}
	return pq[i].posY < pq[j].posY
}

func (pq CartContainer) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}
