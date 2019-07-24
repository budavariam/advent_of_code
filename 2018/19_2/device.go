package main

import "fmt"

// Device is the representation of the wrist device
type Device struct {
	registers    [6]int
	instructions []Instruction
	ipBoundTo    int
	ip           int
}

func (d Device) isEqual(other Device) bool {
	for i, value := range d.registers {
		if other.registers[i] != value {
			return false
		}
	}
	return true
}

var operationsMapping = map[string]func(Instruction, int){
	"addr": addr,
	"setr": setr,
	"muli": muli,
	"seti": seti,
	"gtrr": gtrr,
	"eqrr": eqrr,
	"mulr": mulr,
	"addi": addi,
}

var n = map[int]string{
	0: "aResult",
	1: "bIncrementer",
	2: "c",
	3: "dExitCond",
	4: "E",
	5: "fStartnumber",
}

var ipBoundTo = 4

// Below are the different operations that can be done on the device

//Addition:

// addr (add register) stores into register C the result of adding register A and register B.
func addr(i Instruction, lineNum int) {
	if i.Cout == ipBoundTo {
		jump := 1 + lineNum
		if i.Ain == ipBoundTo {
			fmt.Printf("addr\t\tGOTO %d + %s \r\n", jump, n[i.Bin])
		} else {
			fmt.Printf("addr\t\tGOTO %d + %s \r\n", jump, n[i.Ain])

		}
	} else if i.Ain == ipBoundTo {
		fmt.Printf("addr\t\t%s := %d + %s \r\n", n[i.Cout], lineNum, n[i.Bin])
	} else if i.Bin == ipBoundTo {
		fmt.Printf("addr\t\t%s := %s + %d \r\n", n[i.Cout], n[i.Ain], lineNum)
	} else {
		fmt.Printf("addr\t\t%s := %s + %s\r\n", n[i.Cout], n[i.Ain], n[i.Bin])
	}
}

//addi (add immediate) stores into register C the result of adding register A and value B.
func addi(i Instruction, lineNum int) {
	if i.Cout == ipBoundTo {
		jump := lineNum + 1
		if i.Ain == ipBoundTo {
			jump += i.Bin
		}
		fmt.Printf("addi\t\tGOTO %d \r\n", jump)
	} else {
		fmt.Printf("addi\t\t%s := %s + %d \r\n", n[i.Cout], n[i.Ain], i.Bin)
	}
}

// Multiplication:

// mulr (multiply register) stores into register C the result of multiplying register A and register B.
func mulr(i Instruction, lineNum int) {
	if i.Cout == ipBoundTo {
		fmt.Printf("mulr\t\tEXIT \r\n")
	} else {
		if i.Ain == ipBoundTo {
			fmt.Printf("mulr\t\t%s := %d * %s \r\n", n[i.Cout], lineNum, n[i.Bin])
		} else if i.Bin == ipBoundTo {
			fmt.Printf("mulr\t\t%s := %s * %d \r\n", n[i.Cout], n[i.Ain], lineNum)
		} else {
			fmt.Printf("mulr\t\t%s := %s * %s \r\n", n[i.Cout], n[i.Ain], n[i.Bin])
		}
	}
}

// muli (multiply immediate) stores into register C the result of multiplying register A and value B.
func muli(i Instruction, lineNum int) {
	fmt.Printf("muli\t\t%s := %s * %d\r\n", n[i.Cout], n[i.Ain], i.Bin)
}

// Assignment:

// setr (set register) copies the contents of register A into register C. (Input B is ignored.)
func setr(i Instruction, lineNum int) {
	if i.Cout == ipBoundTo {
		fmt.Printf("setr\t\tGOTO %d \r\n", i.Ain)
	} else if i.Ain == ipBoundTo {
		fmt.Printf("setr\t\t%s = %d\r\n", n[i.Cout], lineNum)
	} else {
		fmt.Printf("setr\t\t%s = %s\r\n", n[i.Cout], n[i.Ain])
	}
}

// seti (set immediate) stores value A into register C. (Input B is ignored.)
func seti(i Instruction, lineNum int) {
	if i.Cout == ipBoundTo {
		fmt.Printf("seti\t\tGOTO %d \r\n", i.Ain+1)
	} else {
		fmt.Printf("seti\t\t%s = %d\r\n", n[i.Cout], i.Ain)
	}
}

// Greater-than testing:

// gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
func gtrr(i Instruction, lineNum int) {
	fmt.Printf("gtrr\t\t%s = (%s > %s) ? 1 : 0\r\n", n[i.Cout], n[i.Ain], n[i.Bin])
}

// Equality testing:

// eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
func eqrr(i Instruction, lineNum int) {
	fmt.Printf("eqrr\t\t%s = (%s == %s) ? 1 : 0\r\n", n[i.Cout], n[i.Ain], n[i.Bin])
}
