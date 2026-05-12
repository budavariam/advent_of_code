use std::{collections::HashSet, fs};

#[derive(Debug)]
enum Action {
    TurnOn,
    TurnOff,
    Toggle,
}

#[derive(Debug)]
struct Instruction {
    action: Action,
    x1: u32,
    y1: u32,
    x2: u32,
    y2: u32,
}

#[derive(Debug)]
struct Matrix {
    data: HashSet<(u32, u32)>,
}

impl Matrix {
    fn new() -> Self {
        Matrix {
            data: HashSet::new(),
        }
    }

    pub fn count_lit(&self) -> u32 {
        self.data.len() as u32
    }

    fn handle(&mut self, instr: Instruction) {
        match instr.action {
            Action::TurnOn => {
                for i in instr.x1..instr.x2 + 1 {
                    for j in instr.y1..instr.y2 + 1 {
                        self.data.insert((i, j));
                    }
                }
            }
            Action::TurnOff => {
                for i in instr.x1..instr.x2 + 1 {
                    for j in instr.y1..instr.y2 + 1 {
                        self.data.remove(&(i, j));
                    }
                }
            }
            Action::Toggle => {
                for i in instr.x1..instr.x2 + 1 {
                    for j in instr.y1..instr.y2 + 1 {
                        match self.data.get(&(i, j)) {
                            Some(_) => {
                                self.data.remove(&(i, j));
                            }
                            None => {
                                self.data.insert((i, j));
                            }
                        }
                    }
                }
            }
        }
    }
}

fn parse_coord(s: &str) -> Option<(u32, u32)> {
    let (a, b) = s.split_once(",")?;
    Some((a.parse().ok()?, b.parse().ok()?))
}

fn parse_line(line: &str) -> Option<Instruction> {
    let (action, rest) = if let Some(r) = line.strip_prefix("turn on ") {
        (Action::TurnOn, r)
    } else if let Some(r) = line.strip_prefix("turn off ") {
        (Action::TurnOff, r)
    } else if let Some(r) = line.strip_prefix("toggle ") {
        (Action::Toggle, r)
    } else {
        return None;
    };

    let (from, to) = rest.split_once(" through ")?;
    let (x1, y1) = parse_coord(from)?;
    let (x2, y2) = parse_coord(to)?;

    Some(Instruction {
        action,
        x1,
        y1,
        x2,
        y2,
    })
}

fn solution(input: &str) -> String {
    let mut matrix = Matrix::new();
    let cnt = input.lines().count();
    for (i, raw_line) in input.lines().enumerate() {
        print!("{}/{}\n", i, cnt);
        if let Some(instr) = parse_line(raw_line) {
            matrix.handle(instr);
        };
    }
    matrix.count_lit().to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
