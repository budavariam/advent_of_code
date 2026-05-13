use std::{collections::HashMap, fs};

#[derive(Debug, Clone, PartialEq, Hash, Eq)]
enum Wire {
    Literal(u16),
    Label(String),
}

impl Wire {
    fn parse(s: &str) -> Self {
        if let Ok(n) = s.trim().parse::<u16>() {
            Wire::Literal(n)
        } else {
            Wire::Label(s.trim().to_string())
        }
    }
}

#[derive(Debug, Clone)]
enum Action {
    And(Wire, Wire),
    Or(Wire, Wire),
    RShift(Wire, Wire),
    LShift(Wire, Wire),
    Not(Wire),
    Assign(Wire),
}

#[derive(Debug, Clone)]
struct Instruction {
    action: Action,
    target: String,
}

fn parse_line(line: &str) -> Option<Instruction> {
    let (left, target) = line.split_once(" -> ")?;
    let target = target.trim().to_string();
    if let Some(l) = left.strip_prefix("NOT ") {
        return Some(Instruction {
            action: Action::Not(Wire::parse(l)),
            target,
        });
    } else if let Some((a, b)) = left.split_once(" OR ") {
        return Some(Instruction {
            action: Action::Or(Wire::parse(a), Wire::parse(b)),
            target,
        });
    } else if let Some((a, b)) = left.split_once(" AND ") {
        return Some(Instruction {
            action: Action::And(Wire::parse(a), Wire::parse(b)),
            target,
        });
    } else if let Some((a, b)) = left.split_once(" RSHIFT ") {
        return Some(Instruction {
            action: Action::RShift(Wire::parse(a), Wire::parse(b)),
            target,
        });
    } else if let Some((a, b)) = left.split_once(" LSHIFT ") {
        return Some(Instruction {
            action: Action::LShift(Wire::parse(a), Wire::parse(b)),
            target,
        });
    } else {
        return Some(Instruction {
            action: Action::Assign(Wire::parse(left)),
            target,
        });
    }
}

struct Machine {
    instructions: HashMap<String, Instruction>,
    registers: HashMap<String, u16>,
}

impl Machine {
    fn new() -> Self {
        Machine {
            instructions: HashMap::new(),
            registers: HashMap::new(),
        }
    }

    fn load(&mut self, instr: Instruction) {
        self.instructions.insert(instr.target.clone(), instr);
    }

    fn resolve(&mut self, wire: &Wire) -> Option<u16> {
        match wire {
            Wire::Literal(n) => Some(*n),
            Wire::Label(name) => {
                if let Some(&v) = self.registers.get(name) {
                    return Some(v);
                }
                let instr = self.instructions.get(name)?.clone();
                let result = match &instr.action {
                    Action::Assign(w) => self.resolve(w)?,
                    Action::Not(w) => !self.resolve(w)?,
                    Action::And(a, b) => self.resolve(a)? & self.resolve(b)?,
                    Action::Or(a, b) => self.resolve(a)? | self.resolve(b)?,
                    Action::RShift(a, b) => self.resolve(a)? >> self.resolve(b)?,
                    Action::LShift(a, b) => self.resolve(a)? << self.resolve(b)?,
                };
                self.registers.insert(name.clone(), result);
                Some(result)
            }
        }
    }
}

fn solution(input: &str, register: &str) -> String {
    let mut machine = Machine::new();
    for line in input.lines() {
        if let Some(instr) = parse_line(line) {
            machine.load(instr);
        }
    }
    machine
        .resolve(&Wire::Label(register.to_string()))
        .map(|v| v.to_string())
        .unwrap_or_else(|| String::from("No result"))
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");

    let answer = solution(&input, "a");
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
