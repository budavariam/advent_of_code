extern crate regex;

use regex::Regex;
use std::{fs, ops::Rem};

fn calc_next(prev: u64) -> u64 {
    // So, to find the second code (which ends up in row 2, column 1), start with the previous value, 20151125. Multiply it by 252533 to get 5088824049625. Then, divide that by 33554393, which leaves a remainder of 31916031. That remainder is the second code.
    (prev * 252533).rem(33554393)
}

fn next_pos((row, col): (u64, u64)) -> (u64, u64) {
    if row == 1 {
        // println!("{}", col + 1);
        return (col + 1, 1);
    }
    (row - 1, col + 1)
}

fn solution(input: &str) -> String {
    let pattern = r"To continue, please consult the code grid in the manual.  Enter the code at row (?P<row>\d+), column (?P<col>\d+).";
    let re = Regex::new(pattern).unwrap();
    let mut curr_pos = (1, 1);
    let mut trgt_pos = (1, 1);

    if let Some(c) = re.captures(input) {
        trgt_pos.0 = c["row"].parse().unwrap();
        trgt_pos.1 = c["col"].parse().unwrap();
    }

    let mut curr = 20151125_u64;
    while curr_pos != trgt_pos {
        // println!("{:?}: {}", curr_pos, curr);
        curr = calc_next(curr);
        curr_pos = next_pos(curr_pos);
    }
    curr.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
