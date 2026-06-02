use std::fs;

fn fuel_for_mass(mass: i32) -> i32 {
    let mut total = 0;
    let mut fuel = mass / 3 - 2;

    while fuel > 0 {
        total += fuel;
        fuel = fuel / 3 - 2;
    }

    total
}

fn solution(input: &str) -> String {
    input
        .lines()
        .filter(|line| !line.trim().is_empty())
        .map(|line| {
            let mass: i32 = line
                .trim()
                .parse()
                .expect("input should contain module masses");
            fuel_for_mass(mass)
        })
        .sum::<i32>()
        .to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
