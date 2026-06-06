use aoc2019::machine::Machine;
use std::fs;

fn solution(input: &str) -> String {
    let code = Machine::parse_program(input);
    let mut machine = Machine::new(code);
    machine.push_input(1);
    machine.start();
    // println!("{:?}", machine);
    machine
        .get_output()
        .iter()
        .map(|x| x.to_string())
        .collect::<Vec<String>>()
        .join(",")
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
