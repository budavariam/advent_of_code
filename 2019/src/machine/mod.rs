use std::collections::VecDeque;

#[derive(Debug, Clone, Copy)]
pub enum Mode {
    Position,
    Immediate,
}

pub struct Machine {
    ip: usize,
    memory: Vec<isize>,
    output: Vec<isize>,
    input: VecDeque<isize>,
}

impl Machine {
    pub fn new(code: Vec<isize>) -> Self {
        Machine {
            ip: 0,
            memory: code,
            output: Vec::new(),
            input: VecDeque::new(),
        }
    }

    pub fn parse_program(input: &str) -> Vec<isize> {
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

    pub fn push_input(&mut self, value: isize) {
        self.input.push_back(value);
    }

    pub fn get_output(&self) -> &Vec<isize> {
        &self.output
    }

    pub fn get_memory_at(&self, i: usize) -> isize {
        self.memory.get(i).cloned().unwrap()
    }

    pub fn parse_opcode(instruction: isize) -> (isize, Vec<Mode>) {
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
    pub fn get_mode(param_modes: &[Mode], index: usize) -> Mode {
        param_modes.get(index).copied().unwrap_or(Mode::Position)
    }

    pub fn read_param(&self, ip: usize, offset: usize, mode: Mode) -> isize {
        match mode {
            Mode::Position => {
                let addr = self.memory[ip + offset] as usize;
                self.memory[addr]
            }
            Mode::Immediate => self.memory[ip + offset],
        }
    }

    pub fn start(&mut self) -> Option<isize> {
        loop {
            let (instruction, param_modes) = Machine::parse_opcode(self.memory[self.ip]);

            match instruction {
                99 => return None,

                1 => {
                    let a = self.read_param(self.ip, 1, Machine::get_mode(&param_modes, 0));
                    let b = self.read_param(self.ip, 2, Machine::get_mode(&param_modes, 1));
                    let pos_target = self.memory[self.ip + 3] as usize;
                    self.memory[pos_target] = a + b;
                    self.ip += 4;
                }

                2 => {
                    let a = self.read_param(self.ip, 1, Machine::get_mode(&param_modes, 0));
                    let b = self.read_param(self.ip, 2, Machine::get_mode(&param_modes, 1));
                    let pos_target = self.memory[self.ip + 3] as usize;
                    self.memory[pos_target] = a * b;
                    self.ip += 4;
                }

                3 => {
                    let pos_target = self.memory[self.ip + 1] as usize;
                    self.memory[pos_target] = self
                        .input
                        .pop_front()
                        .expect("input queue is empty but opcode 3 was reached");
                    self.ip += 2;
                }

                4 => {
                    let value = self.read_param(self.ip, 1, Machine::get_mode(&param_modes, 0));
                    self.output.push(value);
                    self.ip += 2;
                    return Some(value);
                }

                /* Opcode 5 is jump-if-true:
                 *      if the first parameter is non-zero,
                 *              it sets the instruction pointer to the value from the second parameter.
                 *      Otherwise, it does nothing. */
                5 => {
                    let a = self.read_param(self.ip, 1, Machine::get_mode(&param_modes, 0));
                    let b = self.read_param(self.ip, 2, Machine::get_mode(&param_modes, 1));
                    if a != 0 {
                        self.ip = b.try_into().unwrap();
                    } else {
                        self.ip += 3;
                    }
                }
                /* Opcode 6 is jump-if-false:
                 *      if the first parameter is zero,
                 *            it sets the instruction pointer to the value from the second parameter.
                 *      Otherwise, it does nothing. */
                6 => {
                    let a = self.read_param(self.ip, 1, Machine::get_mode(&param_modes, 0));
                    let b = self.read_param(self.ip, 2, Machine::get_mode(&param_modes, 1));
                    if a == 0 {
                        self.ip = b.try_into().unwrap();
                    } else {
                        self.ip += 3;
                    }
                }
                /* Opcode 7 is less than:
                 *      if the first parameter is less than the second parameter,
                 *          it stores 1 in the position given by the third parameter.
                 *      Otherwise, it stores 0. */
                7 => {
                    let a = self.read_param(self.ip, 1, Machine::get_mode(&param_modes, 0));
                    let b = self.read_param(self.ip, 2, Machine::get_mode(&param_modes, 1));
                    let pos_target = self.memory[self.ip + 3] as usize;
                    self.memory[pos_target] = if a < b { 1 } else { 0 };
                    self.ip += 4;
                }
                /* Opcode 8 is equals:
                 *      if the first parameter is equal to the second parameter,
                 *          it stores 1 in the position given by the third parameter.
                 *      Otherwise, it stores 0.
                 */
                8 => {
                    let a = self.read_param(self.ip, 1, Machine::get_mode(&param_modes, 0));
                    let b = self.read_param(self.ip, 2, Machine::get_mode(&param_modes, 1));
                    let pos_target = self.memory[self.ip + 3] as usize;
                    self.memory[pos_target] = if a == b { 1 } else { 0 };
                    self.ip += 4;
                }
                _ => panic!("Unknown opcode {} at ip {}", instruction, self.ip),
            }
        }
    }
}
