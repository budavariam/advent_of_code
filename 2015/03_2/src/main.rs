use std::{collections::HashSet, fs};

#[derive(Eq, PartialEq, Debug, Hash, Copy, Clone)]
struct Position {
    x: i32,
    y: i32,
}

impl Position {
    fn step(&mut self, direction: char) {
        match direction {
            '^' => {
                self.y -= 1;
            }
            '>' => {
                self.x += 1;
            }
            'v' => {
                self.y += 1;
            }
            '<' => {
                self.x -= 1;
            }
            _ => (),
        }
    }
}

fn solution(input: &str) -> String {
    let mut santa_curr_pos = Position { x: 0, y: 0 };
    let mut robo_curr_pos = Position { x: 0, y: 0 };
    let mut visited: HashSet<Position> = HashSet::new();
    visited.insert(santa_curr_pos);

    for (i, ch) in input.chars().enumerate() {
        let pos = if i % 2 == 0 {
            &mut santa_curr_pos
        } else {
            &mut robo_curr_pos
        };
        pos.step(ch);
        visited.insert(*pos);
    }
    visited.len().to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
