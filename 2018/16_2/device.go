package main

import "strconv"

// Device is the representation of the wrist device
type Device [4]int

func (d Device) isEqual(other Device) bool {
	for i, value := range d {
		if other[i] != value {
			return false
		}
	}
	return true
}

func initDevice(strslice []string) Device {
	result := Device{}
	for i := 0; i < 4; i++ {
		result[i], _ = strconv.Atoi(strslice[i])
	}
	return result
}

// Below are the different operations that can be done on the device

//Addition:

// addr (add register) stores into register C the result of adding register A and register B.
func addr(i Instruction, d Device) Device {
	d[i.Cout] = d[i.Ain] + d[i.Bin]
	return d
}

//addi (add immediate) stores into register C the result of adding register A and value B.
func addi(i Instruction, d Device) Device {
	d[i.Cout] = d[i.Ain] + i.Bin
	return d
}

// Multiplication:

// mulr (multiply register) stores into register C the result of multiplying register A and register B.
func mulr(i Instruction, d Device) Device {
	d[i.Cout] = d[i.Ain] * d[i.Bin]
	return d
}

// muli (multiply immediate) stores into register C the result of multiplying register A and value B.
func muli(i Instruction, d Device) Device {
	d[i.Cout] = d[i.Ain] * i.Bin
	return d
}

// Bitwise AND:

// banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
func banr(i Instruction, d Device) Device {
	d[i.Cout] = d[i.Ain] & d[i.Bin]
	return d
}

// bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
func bani(i Instruction, d Device) Device {
	d[i.Cout] = d[i.Ain] & i.Bin
	return d
}

// Bitwise OR:

// borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
func borr(i Instruction, d Device) Device {
	d[i.Cout] = d[i.Ain] | d[i.Bin]
	return d
}

// bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
func bori(i Instruction, d Device) Device {
	d[i.Cout] = d[i.Ain] | i.Bin
	return d
}

// Assignment:

// setr (set register) copies the contents of register A into register C. (Input B is ignored.)
func setr(i Instruction, d Device) Device {
	d[i.Cout] = d[i.Ain]
	return d
}

// seti (set immediate) stores value A into register C. (Input B is ignored.)
func seti(i Instruction, d Device) Device {
	d[i.Cout] = i.Ain
	return d
}

// Greater-than testing:

// gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
func gtir(i Instruction, d Device) Device {
	if i.Ain > d[i.Bin] {
		d[i.Cout] = 1
	} else {
		d[i.Cout] = 0
	}
	return d
}

// gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
func gtri(i Instruction, d Device) Device {
	if d[i.Ain] > i.Bin {
		d[i.Cout] = 1
	} else {
		d[i.Cout] = 0
	}
	return d
}

// gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
func gtrr(i Instruction, d Device) Device {
	if d[i.Ain] > d[i.Bin] {
		d[i.Cout] = 1
	} else {
		d[i.Cout] = 0
	}
	return d
}

// Equality testing:

// eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
func eqir(i Instruction, d Device) Device {
	if i.Ain == d[i.Bin] {
		d[i.Cout] = 1
	} else {
		d[i.Cout] = 0
	}
	return d
}

// eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
func eqri(i Instruction, d Device) Device {
	if d[i.Ain] == i.Bin {
		d[i.Cout] = 1
	} else {
		d[i.Cout] = 0
	}
	return d
}

// eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
func eqrr(i Instruction, d Device) Device {
	if d[i.Ain] == d[i.Bin] {
		d[i.Cout] = 1
	} else {
		d[i.Cout] = 0
	}
	return d
}
