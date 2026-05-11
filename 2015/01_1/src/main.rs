use std::fs;

fn solution(input: &str) -> String {
    let mut floor = 0;

    for ch in input.chars() {
        match ch {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => {}
        }
    }

    floor.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let solution = solution(&input);

    println!("Part 1: {}", solution);
}

#[cfg(test)]
mod main_tests;
