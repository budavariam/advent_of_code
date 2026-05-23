use std::{collections::HashMap, fs};

fn solution(input: &str, eggnog: u32) -> String {
    let buckets = input
        .lines()
        .map(|e| e.parse().unwrap())
        .collect::<Vec<u32>>();
    let cnt = buckets.len();
    let mut result_histogram: HashMap<u32, u32> = HashMap::new();

    for i in 0..2u32.pow(cnt as u32) {
        let binrepr = &format!("{i:#034b}").chars().rev().collect::<Vec<_>>()[..cnt as usize];
        let sum: u32 = binrepr
            .iter()
            .enumerate()
            .map(|(i, consider)| {
                if *consider == '1' {
                    *buckets.get(i).unwrap()
                } else {
                    0
                }
            })
            .sum();
        if sum == eggnog {
            let container_cnt = binrepr.iter().filter(|c| **c == '1').count() as u32;
            result_histogram
                .entry(container_cnt)
                .and_modify(|f| {
                    *f += 1;
                })
                .or_insert(1);
        }
    }
    let lowest_key = result_histogram.keys().min().unwrap();
    let result = result_histogram.get(lowest_key).unwrap();
    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, 150);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
