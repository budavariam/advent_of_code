extern crate itertools;

use aoc2019::machine::Machine;
use itertools::Itertools;
use std::fs;

fn amplifier(code: &Vec<isize>, phase: isize, input: isize) -> isize {
    let mut machine = Machine::new(code.clone());
    machine.push_input(phase);
    machine.push_input(input);
    machine.start();
    machine
        .get_output()
        .last()
        .copied()
        .expect("Output missing")
}

fn amplifier_queue(code: &Vec<isize>, sequence: Vec<&isize>) -> isize {
    let mut output: isize = 0;
    for phase_setting in sequence {
        output = amplifier(&code, *phase_setting, output);
        // println!("{}", output);
    }
    output
}

fn solution(input: &str) -> String {
    let code = Machine::parse_program(input);
    let numbers: Vec<isize> = vec![0, 1, 2, 3, 4];
    // for seq in numbers.iter().permutations(5) {
    //     let res = ;
    //     println!("{}", res);
    // }
    let result = numbers
        .iter()
        .permutations(5)
        .map(|seq| amplifier_queue(&code, seq))
        .max()
        .unwrap_or_else(|| -1);

    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
