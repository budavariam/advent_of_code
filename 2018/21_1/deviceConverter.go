package main

import "fmt"

// DeviceConverter is the representation of the wrist deviceConverter
type DeviceConverter struct {
	registers    [6]int
	instructions []Instruction
	ipBoundTo    int
	ip           int
}

func (d DeviceConverter) isEqual(other DeviceConverter) bool {
	for i, value := range d.registers {
		if other.registers[i] != value {
			return false
		}
	}
	return true
}

var operationsConvertMapping = map[string]func(Instruction, int){
	"addr": addrConvert,
	"setr": setrConvert,
	"muli": muliConvert,
	"seti": setiConvert,
	"gtrr": gtrrConvert,
	"gtir": gtirConvert,
	"eqrr": eqrrConvert,
	"eqri": eqriConvert,
	"mulr": mulrConvert,
	"addi": addiConvert,
	"banr": banrConvert,
	"bani": baniConvert,
	"borr": borrConvert,
	"bori": boriConvert,
}

var n = map[int]string{
	0: "a",
	1: "b",
	2: "c",
	3: "d",
	4: "e",
	5: "F",
}

var ipBoundTo = 5

// Below are the different operations that can be done on the deviceConverter

//Addition:

// addr (add register) stores into register C the result of adding register A and register B.
func addrConvert(i Instruction, lineNum int) {
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
func addiConvert(i Instruction, lineNum int) {
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
func mulrConvert(i Instruction, lineNum int) {
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
func muliConvert(i Instruction, lineNum int) {
	fmt.Printf("muli\t\t%s := %s * %d\r\n", n[i.Cout], n[i.Ain], i.Bin)
}

// Assignment:

// setr (set register) copies the contents of register A into register C. (Input B is ignored.)
func setrConvert(i Instruction, lineNum int) {
	if i.Cout == ipBoundTo {
		fmt.Printf("setr\t\tGOTO %d \r\n", i.Ain)
	} else if i.Ain == ipBoundTo {
		fmt.Printf("setr\t\t%s = %d\r\n", n[i.Cout], lineNum)
	} else {
		fmt.Printf("setr\t\t%s = %s\r\n", n[i.Cout], n[i.Ain])
	}
}

// seti (set immediate) stores value A into register C. (Input B is ignored.)
func setiConvert(i Instruction, lineNum int) {
	if i.Cout == ipBoundTo {
		fmt.Printf("seti\t\tGOTO %d \r\n", i.Ain+1)
	} else {
		fmt.Printf("seti\t\t%s = %d\r\n", n[i.Cout], i.Ain)
	}
}

// Greater-than testing:

// gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
func gtrrConvert(i Instruction, lineNum int) {
	fmt.Printf("gtrr\t\t%s = (%s > %s) ? 1 : 0\r\n", n[i.Cout], n[i.Ain], n[i.Bin])
}

// gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
func gtirConvert(i Instruction, lineNum int) {
	fmt.Printf("gtir\t\t%s = (%d > %s) ? 1 : 0\r\n", n[i.Cout], i.Ain, n[i.Bin])
}

// Equality testing:

// eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
func eqrrConvert(i Instruction, lineNum int) {
	fmt.Printf("eqrr\t\t%s = (%s == %s) ? 1 : 0\r\n", n[i.Cout], n[i.Ain], n[i.Bin])
}

// eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
func eqriConvert(i Instruction, lineNum int) {
	fmt.Printf("eqri\t\t%s = (%s == %d) ? 1 : 0\r\n", n[i.Cout], n[i.Ain], i.Bin)
}

// Bitwise AND:

// banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
func banrConvert(i Instruction, lineNum int) {
	fmt.Printf("banr\t\t%s = %s & %s\r\n", n[i.Cout], n[i.Ain], n[i.Bin])
}

// bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
func baniConvert(i Instruction, lineNum int) {
	fmt.Printf("bani\t\t%s = %s & %d\r\n", n[i.Cout], n[i.Ain], i.Bin)
}

// Bitwise OR:

// borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
func borrConvert(i Instruction, lineNum int) {
	fmt.Printf("borr\t\t%s = %s | %s\r\n", n[i.Cout], n[i.Ain], n[i.Bin])
}

// bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
func boriConvert(i Instruction, lineNum int) {
	fmt.Printf("bori\t\t%s = %s | %d\r\n", n[i.Cout], n[i.Ain], i.Bin)
}
