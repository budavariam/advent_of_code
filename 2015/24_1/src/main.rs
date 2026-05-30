extern crate itertools;
use itertools::Itertools;
use std::fs;

fn can_split_into_two(items: &[u64], target: u64) -> bool {
    for size in 1..=items.len() {
        for combo in items.iter().combinations(size) {
            if combo.iter().copied().sum::<u64>() == target {
                return true;
            }
        }
    }
    false
}

fn solution(input: &str) -> String {
    let numbers: Vec<u64> = input
        .lines()
        .filter_map(|e| e.trim().parse().ok())
        .collect();
    let bin_size: u64 = numbers.iter().sum::<u64>() / 3;

    for bin_1_size in 1..=numbers.len() {
        for combo1_indices in (0..numbers.len()).combinations(bin_1_size) {
            let combo1: Vec<u64> = combo1_indices.iter().map(|&i| numbers[i]).collect();
            if combo1.iter().sum::<u64>() != bin_size {
                continue; // bin 1 not filled
            }

            let rest_items: Vec<u64> = (0..numbers.len())
                .filter(|i| !combo1_indices.contains(i))
                .map(|i| numbers[i])
                .collect();

            if can_split_into_two(&rest_items, bin_size) {
                return combo1.iter().product::<u64>().to_string();
            }
        }
    }

    0.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
