use std::{collections::HashMap, fs, ops::Div};

struct Machine {
    instruction_ptr: i32,
    registers: HashMap<char, i32>,
    instructions: Vec<Instruction>,
}

impl Machine {
    fn new() -> Self {
        Machine {
            instruction_ptr: 0,
            registers: HashMap::new(),
            instructions: Vec::new(),
        }
    }

    fn register_instruction(&mut self, instruction: Instruction) {
        self.instructions.push(instruction);
    }

    fn eval(&mut self) {
        let instruction = self
            .instructions
            .get_mut(self.instruction_ptr as usize)
            .unwrap();
        // println!("{:?}", instruction);

        match instruction {
            // inc r increments register r, adding 1 to it, then continues with the next instruction.
            Instruction::INC { r } => {
                self.registers
                    .entry(*r)
                    .and_modify(|x| *x += 1)
                    .or_insert(1);
            }
            // hlf r sets register r to half its current value, then continues with the next instruction.
            Instruction::HLF { r } => {
                self.registers
                    .entry(*r)
                    .and_modify(|x| *x = x.div(2))
                    .or_insert(0);
            }
            // tpl r sets register r to triple its current value, then continues with the next instruction.
            Instruction::TPL { r } => {
                self.registers
                    .entry(*r)
                    .and_modify(|x| *x *= 3)
                    .or_insert(0);
            }
            // jmp offset is a jump; it continues with the instruction offset away relative to itself.
            Instruction::JMP { offset } => {
                self.instruction_ptr += *offset - 1;
            }
            // jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
            Instruction::JIE { r, offset } => {
                if let Some(x) = self.registers.get(&r) {
                    if x % 2 == 0 {
                        self.instruction_ptr += *offset - 1;
                    }
                }
            }
            // jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
            Instruction::JIO { r, offset } => {
                if let Some(x) = self.registers.get(&r) {
                    if *x == 1 {
                        self.instruction_ptr += *offset - 1;
                    }
                }
            }
        }
        self.instruction_ptr += 1;
    }

    fn run(&mut self) {
        while self.instruction_ptr < self.instructions.len() as i32 {
            self.eval();
        }
    }
}

#[derive(Debug)]
enum Instruction {
    HLF { r: char },
    TPL { r: char },
    INC { r: char },
    JMP { offset: i32 },
    JIE { r: char, offset: i32 },
    JIO { r: char, offset: i32 },
}

impl Instruction {
    fn parse(input: &str) -> Self {
        let parts: Vec<&str> = input.split_whitespace().collect();
        let instruction_name = *parts.first().unwrap();
        if instruction_name == "inc" {
            Instruction::INC {
                r: parts.get(1).unwrap().chars().next().unwrap(),
            }
        } else if instruction_name == "hlf" {
            Instruction::HLF {
                r: parts.get(1).unwrap().chars().next().unwrap(),
            }
        } else if instruction_name == "tpl" {
            Instruction::TPL {
                r: parts.get(1).unwrap().chars().next().unwrap(),
            }
        } else if instruction_name == "jmp" {
            Instruction::JMP {
                offset: parts.get(1).unwrap().parse().unwrap(),
            }
        } else if instruction_name == "jie" {
            Instruction::JIE {
                r: parts.get(1).unwrap().chars().next().unwrap(),
                offset: parts.get(2).unwrap().parse().unwrap(),
            }
        } else if instruction_name == "jio" {
            Instruction::JIO {
                r: parts.get(1).unwrap().chars().next().unwrap(),
                offset: parts.get(2).unwrap().parse().unwrap(),
            }
        } else {
            panic!("Unknown instruction.");
        }
    }
}

fn solution(input: &str, result_register: char) -> String {
    let mut machine = Machine::new();
    for line in input.lines() {
        let inst = Instruction::parse(line);
        machine.register_instruction(inst);
    }

    machine.run();
    let result = machine.registers.get(&result_register).unwrap();

    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, 'b');
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
