use std::fs;

fn solution(input: &str) -> String {
    input
        .lines()
        .filter(|line| !line.trim().is_empty())
        .map(|line| {
            let mass: i32 = line
                .trim()
                .parse()
                .expect("input should contain module masses");
            mass / 3 - 2
        })
        .sum::<i32>()
        .to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let solution = solution(&input);

    println!("Answer: {}", solution);
}

#[cfg(test)]
mod main_tests;
