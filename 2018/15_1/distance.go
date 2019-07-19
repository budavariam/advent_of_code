package main

type distanceData struct {
	distance   int
	point      point
	startPoint point
	directions []int
}

type distanceDataList []distanceData

// Sort points
func (ddl distanceDataList) Len() int {
	return len(ddl)
}

func (ddl distanceDataList) Less(i, j int) bool {
	if ddl[i].distance == ddl[j].distance {
		return ddl[i].point.lessThan(ddl[j].point)
	}
	return ddl[i].distance < ddl[j].distance
}

func (ddl distanceDataList) Swap(i, j int) {
	ddl[j], ddl[i] = ddl[i], ddl[j]
}

type pathNode struct {
	step     int
	nextStep point
	goal     point
}

type pathNodeList []pathNode

// Sort units
func (u pathNodeList) Len() int {
	return len(u)
}
func (u pathNodeList) Less(i, j int) bool {
	if u[i].step == u[j].step {
		return u[i].goal.lessThan(u[j].goal)
	}
	return u[i].step < u[j].step
}
func (u pathNodeList) Swap(i, j int) {
	u[j], u[i] = u[i], u[j]
}