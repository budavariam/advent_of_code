use std::fs;

fn solution(input: &str, eggnog: u32) -> String {
    let mut result = 0;
    let buckets = input
        .lines()
        .map(|e| e.parse().unwrap())
        .collect::<Vec<u32>>();
    let cnt = buckets.len();
    // 1. go through 0 to 2^{numbuckets}
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
        // println!("{:?}: {} == {} ({})", binrepr, sum, eggnog, sum == eggnog);
        if sum == eggnog {
            result += 1;
        }
    }
    // 2. use the current number as a bitmask and sum the corresponding values
    // 3. if it matches add to the result cnt

    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, 150);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
