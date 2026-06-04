extern crate itertools;

use aoc2019::machine::Machine;
use itertools::{Itertools, enumerate};
use std::fs;

fn amplifier(machine: &mut Machine, input: isize) -> Option<isize> {
    machine.push_input(input);
    machine.start()
}

fn amplifier_loop(code: &Vec<isize>, sequence: Vec<isize>) -> isize {
    let mut machines: Vec<Machine> = (&sequence)
        .iter()
        .map(|phase_setting| {
            let mut m = Machine::new(code.clone());
            m.push_input(*phase_setting);
            m
        })
        .collect();

    let mut output: isize = 0;
    'outer: loop {
        for (i, _) in enumerate(&sequence) {
            match amplifier(&mut machines[i], output) {
                Some(out) => {
                    output = out;
                }
                None => {
                    break 'outer;
                }
            }
            // println!("{}", output);
        }
    }
    output
}

fn solution(input: &str) -> String {
    let code = Machine::parse_program(input);
    let result = (5_isize..=9_isize)
        .permutations(5)
        .map(|seq| amplifier_loop(&code, seq))
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
