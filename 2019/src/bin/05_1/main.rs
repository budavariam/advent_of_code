use std::fs;

#[derive(Debug, Clone, Copy)]
enum Mode {
    Position,
    Immediate,
}

struct Machine {
    memory: Vec<isize>,
    output: Vec<isize>,
}

impl Machine {
    fn new(code: Vec<isize>) -> Self {
        Machine {
            memory: code,
            output: Vec::new(),
        }
    }

    fn parse_opcode(instruction: isize) -> (isize, Vec<Mode>) {
        let opcode = instruction % 100;
        let mut modes_num = instruction / 100;
        let mut param_modes = Vec::new();

        while modes_num > 0 {
            let mode = match modes_num % 10 {
                1 => Mode::Immediate,
                _ => Mode::Position,
            };
            param_modes.push(mode);
            modes_num /= 10;
        }

        (opcode, param_modes)
    }
    fn get_mode(param_modes: &[Mode], index: usize) -> Mode {
        param_modes.get(index).copied().unwrap_or(Mode::Position)
    }

    fn read_param(&self, ip: usize, offset: usize, mode: Mode) -> isize {
        match mode {
            Mode::Position => {
                let addr = self.memory[ip + offset] as usize;
                self.memory[addr]
            }
            Mode::Immediate => self.memory[ip + offset],
        }
    }

    fn interpret_int_code(&mut self, input: isize) -> Vec<isize> {
        let mut ip = 0;

        loop {
            let (instruction, param_modes) = Machine::parse_opcode(self.memory[ip]);

            match instruction {
                99 => return self.memory.clone(),

                1 => {
                    let a = self.read_param(ip, 1, Machine::get_mode(&param_modes, 0));
                    let b = self.read_param(ip, 2, Machine::get_mode(&param_modes, 1));
                    let pos_target = self.memory[ip + 3] as usize;
                    self.memory[pos_target] = a + b;
                    ip += 4;
                }

                2 => {
                    let a = self.read_param(ip, 1, Machine::get_mode(&param_modes, 0));
                    let b = self.read_param(ip, 2, Machine::get_mode(&param_modes, 1));
                    let pos_target = self.memory[ip + 3] as usize;
                    self.memory[pos_target] = a * b;
                    ip += 4;
                }

                3 => {
                    let pos_target = self.memory[ip + 1] as usize;
                    self.memory[pos_target] = input;
                    ip += 2;
                }

                4 => {
                    let value = self.read_param(ip, 1, Machine::get_mode(&param_modes, 0));
                    self.output.push(value);
                    ip += 2;
                }

                _ => panic!("Unknown opcode {} at ip {}", instruction, ip),
            }
        }
    }
}

fn parse_program(input: &str) -> Vec<isize> {
    input
        .trim()
        .split(',')
        .map(|s| {
            s.trim()
                .parse::<isize>()
                .unwrap_or_else(|_| panic!("failed to parse token: {:?}", s))
        })
        .collect()
}

fn solution(input: &str) -> String {
    let code = parse_program(input);
    let mut machine = Machine::new(code);
    machine.interpret_int_code(1);

    machine
        .output
        .last()
        .copied()
        .unwrap_or(machine.memory[0])
        .to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
