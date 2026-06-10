use std::collections::HashMap;
use std::fs;

use aoc2019::machine::{Machine, StepResult};

type Position = (isize, isize);

#[derive(Debug)]
enum Object {
    Empty,
    Wall,
    Block,
    HorizontalPaddle,
    Ball,
}

impl Object {
    fn parse(object_type: isize) -> Self {
        match object_type {
            1 => Object::Wall,
            2 => Object::Block,
            3 => Object::HorizontalPaddle,
            4 => Object::Ball,
            _ => Object::Empty,
        }
    }
}

fn solution(input: &str) -> String {
    let mut score = 0;
    let code = Machine::parse_program(input);
    let mut m = Machine::new(code);
    let mut buffer: HashMap<Position, Object> = HashMap::new();

    let mut ball_x = 0;
    let mut paddle_x = 0;
    let mut out = Vec::with_capacity(3);

    m.set_memory_at(0, 2);

    loop {
        match m.step() {
            StepResult::Output(v) => {
                out.push(v);

                if out.len() == 3 {
                    let left = out[0];
                    let top = out[1];
                    let value = out[2];
                    out.clear();

                    if left == -1 && top == 0 {
                        score = value;
                        continue;
                    }

                    let object = Object::parse(value);

                    if matches!(object, Object::Ball) {
                        ball_x = left;
                    }
                    if matches!(object, Object::HorizontalPaddle) {
                        paddle_x = left;
                    }

                    buffer.insert((left, top), object);
                }
            }
            StepResult::NeedsInput => {
                m.push_input((ball_x - paddle_x).signum());
            }
            StepResult::Halted => break,
        }
    }

    score.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
