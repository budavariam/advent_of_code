use std::fs;

fn solution(input: &str) -> String {
    let mut floor = 0;
    let mut i = 0;
    for ch in input.chars() {
        i += 1;
        match ch {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => {}
        }
        if floor == -1 {
            break;
        }
    }

    i.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let solution = solution(&input);

    println!("Part 2: {}", solution);
}

#[cfg(test)]
mod main_tests;
